class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # 1. hash-map: time O(n) space O(n)
        # if nums == []:
        #     return -1
        
        # dict = {}
        # for i in range(len(nums)):
        #     if nums[i] in dict:
        #         return nums[i]
        #     else:
        #         dict[nums[i]] = 1
        
        # return -1

        # 2. sort: time O(nlogn) space O(1)
        # if nums == []:
        #     return -1
        
        # nums.sort();

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
            
        # return -1

        # 3. time O(n) space O(1)
        if nums == []:
            return -1
        
        for i in range(len(nums)):
            while nums[i] != i:
                index = nums[i]
                if nums[index] == index:
                    return index
                nums[i], nums[index] = nums[index], nums[i]
        
