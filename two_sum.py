def twoSum(nums, target):   
    for idx, num in enumerate(nums):
        diff = target-num
        if diff in nums and nums.index(diff) != idx:
            return [idx, nums.index(diff)]
            