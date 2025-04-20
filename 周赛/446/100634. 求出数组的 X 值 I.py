class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        pre = [0] * n
        res = [0] * k
        pre[0] = nums[0]
        for i in range(1, n) :
            pre[i] = pre[i - 1] * nums[i]
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if (j - i >= 0):
                    if i == 0 :
                        tmp = pre[j]
                    else :
                        tmp = pre[j] // pre[i - 1]
                    r = tmp % k
                    res[r] += 1
        return res
