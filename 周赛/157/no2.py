from mytools import *
class Solution:
    def maxSubstrings(self, word: str) -> int:
        hash = defaultdict(list)
        for i in range(len(word)):
            hash[word[i]].append(i)
        