class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_map={}

        for i in range(len(nums)):
            complement=target-nums[i]

            if complement in ans_map:
                return [ans_map[complement], i]
            else:
                ans_map[nums[i]]=i
        return []
        