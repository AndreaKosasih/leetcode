class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Example usage
solution = Solution()

s1 = "abcabcbb"
print(solution.lengthOfLongestSubstring(s1))  # Output: 3

s2 = "bbbbb"
print(solution.lengthOfLongestSubstring(s2))  # Output: 1

s3 = "pwwkew"
print(solution.lengthOfLongestSubstring(s3))  # Output: 3
