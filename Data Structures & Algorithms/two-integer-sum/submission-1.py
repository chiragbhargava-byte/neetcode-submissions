class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_set = {}

        for i, num in enumerate(nums):
            remain = target - num

            if remain in hash_set:
                return [hash_set[remain], i]
            
            hash_set[num] = i
        