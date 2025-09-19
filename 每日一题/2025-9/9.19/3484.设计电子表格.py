#
# @lc app=leetcode.cn id=3484 lang=python3
#
# [3484] 设计电子表格
#

# @lc code=start
class Spreadsheet:

    def __init__(self, rows: int):
        self.excel = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        idx = ""
        for i in range(1, len(cell)):
            idx += cell[i]
        self.excel[int(idx) - 1][ord(cell[0]) - ord("A")] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        a1 = ""
        a2 = ""
        n = len(formula)
        for i in range(1, n):
            if formula[i] == "+": break
            a1 += formula[i]
        for j in range(i + 1, n):
            a2 += formula[j]
        
        
        def get(a1):
            x = 0
            if a1.isdigit():
                x += int(a1)
            else:
                idx = ""
                for i in range(1, len(a1)):
                    idx += a1[i]
                x += self.excel[int(idx) - 1][ord(a1[0]) - ord("A")]
            return x
        return get(a1) + get(a2)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
# @lc code=end

