class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}  # Bản đồ lưu trữ chỉ mục cuối cùng của mỗi ký tự
        start = 0  # Bắt đầu chuỗi con hiện tại
        max_length = 0  # Độ dài tối đa của chuỗi con không lặp lại ký tự

        for end in range(len(s)):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                # Nếu ký tự được lặp lại và lần xuất hiện cuối cùng của nó nằm trong chuỗi con hiện tại
                start = char_index_map[s[end]] + 1

            char_index_map[s[end]] = end
            current_length = end - start + 1
            max_length = max(max_length, current_length)

        return max_length

# Example usage
s = "abcabcbb"
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)  # Output: 1
