def solve(nums):
    if not nums: return 0
    cur = res = nums[0]
    for x in nums[1:]:
        cur = max(cur + x, x)
        res = max(res, cur)
    return res
