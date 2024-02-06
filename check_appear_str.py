class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Nếu needle là một chuỗi rỗng, trả về 0
        if not needle:
            return 0
        
        # Lặp qua chuỗi "haystack" bằng cách sử dụng cửa sổ trượt có độ dài bằng độ dài của "needle"
        for i in range(len(haystack) - len(needle) + 1):
            # Kiểm tra xem chuỗi con của "haystack" có khớp với "needle" không
            if haystack[i:i+len(needle)] == needle:
                return i  # Trả về chỉ số nếu tìm thấy khớp
        
        # Nếu không tìm thấy khớp nào, trả về -1
        return -1

# Sử dụng ví dụ:
solution = Solution()
haystack = "sadbutsad"
needle = "sad11"
output = solution.strStr(haystack, needle)
print(output)
