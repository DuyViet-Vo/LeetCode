class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Loại bỏ bất kỳ dấu cách cuối cùng nào
        s = s.rstrip()
        
        # Khởi tạo một biến để lưu độ dài của từ cuối cùng
        length_last_word = 0
        
        # Lặp qua các ký tự trong chuỗi từ phải qua trái
        for char in reversed(s):
            # Nếu gặp một dấu cách và độ dài của từ cuối cùng lớn hơn 0, ta đã tìm thấy từ cuối cùng
            if char == ' ' and length_last_word > 0:
                break
            # Nếu ký tự không phải là dấu cách, tăng độ dài của từ cuối cùng
            elif char != ' ':
                length_last_word += 1
        
        # Trả về độ dài của từ cuối cùng
        return length_last_word

solution = Solution()

# Chuỗi đầu vào
input_string = "Hello World"

# Tính độ dài của từ cuối cùng trong chuỗi và in ra màn hình
print("Độ dài của từ cuối cùng trong chuỗi là:", solution.lengthOfLastWord(input_string))