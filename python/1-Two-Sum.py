class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}  # Create a hash map to store the number and its index
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_to_index:
                return [num_to_index[difference], i]
            num_to_index[num] = i

# Create an instance of the Solution class
solution = Solution()

nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1]
