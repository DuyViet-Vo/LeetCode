from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Nếu vòng lặp kết thúc, tức là không tìm thấy target
        # Biến 'left' chính là vị trí đúng để chèn target
        return left

# Sử dụng ví dụ
nums = [1, 3, 5, 6]
target = 5
sol = Solution()
print(sol.searchInsert(nums, target))  # Output: 2
