class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        newarray = [nums[0]]
        for x in range(1, len(nums)):
            if nums[x] in newarray:
                return True
            newarray.append(nums[x])
        return False