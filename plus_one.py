from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Bắt đầu từ chữ số bên phải nhất
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                # Tăng giá trị của chữ số hiện tại lên 1
                digits[i] += 1
                return digits
            else:
                # Đặt chữ số hiện tại thành 0 và di chuyển sang trái
                digits[i] = 0
        
        # Nếu tất cả các chữ số đều là 9, chúng ta cần thêm một chữ số 1 mới ở đầu
        digits.insert(0, 1)
        return digits

# Ví dụ sử dụng:
digits = [1, 2, 3]
solution = Solution()
result = solution.plusOne(digits)
print(result)  # Output: [1, 2, 4]
