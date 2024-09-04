class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        
        start, end = 0, 0

        for i in range(len(s)):
            print("i", i)
            len1 = self.expand_around_center(s, i, i) 
            print("len1: ", len1)
            len2 = self.expand_around_center(s, i, i + 1) 
            print("Len2", len2)
            max_len = max(len1, len2)
            print("Max Len", max_len)
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                print("start,end : ", start,end) 
        print("Start : End", start, end)
        return s[start:end + 1]

    def expand_around_center(self, s, left, right):
        """
        :type s: str
        :type left: int
        :type right: int
        :rtype: int
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

# Ví dụ sử dụng
solution = Solution()

# Ví dụ 1
s1 = "babad"
result1 = solution.longestPalindrome(s1)
print(f"Chuỗi đối xứng dài nhất trong '{s1}' là: '{result1}'")
# Output có thể là "bab" hoặc "aba"

# # Ví dụ 2
# s2 = "cbbd"
# result2 = solution.longestPalindrome(s2)
# print(f"Chuỗi đối xứng dài nhất trong '{s2}' là: '{result2}'")
# # Output: "bb"

# # Ví dụ 3
# s3 = "a"
# result3 = solution.longestPalindrome(s3)
# print(f"Chuỗi đối xứng dài nhất trong '{s3}' là: '{result3}'")
# # Output: "a"

# # Ví dụ 4
# s4 = "ac"
# result4 = solution.longestPalindrome(s4)
# print(f"Chuỗi đối xứng dài nhất trong '{s4}' là: '{result4}'")
# Output: "a" hoặc "c"
