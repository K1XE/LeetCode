import torch

from torch import Tensor, nn
import torch.nn.functional as F

class GQA(nn.Module):
    def __init__(self, num_heads, num_groups, hidden_dim) -> None:
        super().__init__()
        assert hidden_dim % num_groups == 0
        self.head_dim = hidden_dim // num_heads
        self.num_heads = num_heads
        self.num_groups = num_groups
        self.q_proj = nn.Linear(hidden_dim, hidden_dim)
        self.k_proj = nn.Linear(hidden_dim, self.num_groups * self.head_dim)
        self.v_proj = nn.Linear(hidden_dim, self.num_groups * self.head_dim)
        self.o_proj = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, X: Tensor):
        bsz, seq_len, hidden_dim = X.shape
        q = self.q_proj(X)
        k = self.k_proj(X)
        v = self.v_proj(X)
        def split_heads(X: Tensor, num_groups=None):
            if num_groups is None:
                X = X.reshape(bsz, seq_len, self.num_heads, -1).transpose(1, 2)
            else:
                X = X.reshape(bsz, seq_len, self.num_groups, -1).transpose(1, 2).expand(-1, -1, self.num_heads // self.num_groups, -1, -1)
                X = X.reshape(bsz, -1, seq_len, self.head_dim)
            return X
        q = split_heads(q) # [bsz, num_heads, seq_len, head_dim]
        k = split_heads(k, self.num_groups) # [bsz, num_heads, seq_len, head_dim]
        v = split_heads(v, self.num_groups) # [bsz, num_heads, seq_len, head_dim]
        # [seq_len, head_dim] @ [head_dim, seq_len] -> num_heads * head_dim * seq_len * seq_len
        attn_scores = torch.matmul(q, k.transpose(-2, -1)) / torch.sqrt(self.head_dim)
        attn_weights = F.softmax(attn_scores, dim=-1) # [bsz, num_heads, seq_len, seq_len]
        
        mid = attn_weights @ v # [bsz, num_heads, seq_len, head_dim]
        # [seq_len, seq_len] @ [seq_len, head_dim] -> num_heads * seq_len * head_dim * seq_len
        mid = mid.transpose(1, 2).reshape(bsz, seq_len, -1) # [bsz, seq_len, hidden_dim]
        
        o = self.o_proj(mid)
        
        return o