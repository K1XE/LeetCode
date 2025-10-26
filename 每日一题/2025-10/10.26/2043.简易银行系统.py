#
# @lc app=leetcode.cn id=2043 lang=python3
#
# [2043] 简易银行系统
#
from mytools import *
# @lc code=start
class Bank:

    def __init__(self, balance: List[int]):
        self.b = balance
        self.n = len(balance)
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        if 0 <= account1 < self.n and 0 <= account2 < self.n:
            if self.b[account1] >= money:
                self.b[account1] -= money
                self.b[account2] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if 0 <= account < self.n:
            self.b[account] += money
            return True
        return False
    
    def withdraw(self, account: int, money: int) -> bool:
        account -= 1
        if 0 <= account < self.n:
            if self.b[account] >= money:
                self.b[account] -= money
                return True
        return False
    


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
# @lc code=end

