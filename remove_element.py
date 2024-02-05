from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Khởi tạo một biến để theo dõi độ dài mới
        new_length = 0
        
        # Duyệt qua các phần tử trong nums
        for num in nums:
            # Nếu phần tử hiện tại không bằng val, cập nhật danh sách
            if num != val:
                nums[new_length] = num
                new_length += 1
        
        # Độ dài mới đại diện cho số lượng phần tử mà không có giá trị được chỉ định
        return new_length

# Sử dụng ví dụ
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
solution = Solution()
result = solution.removeElement(nums, val)

print(f"Output: {result}, nums = {nums[:result]}")
