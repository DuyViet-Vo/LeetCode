from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_all = sum(nums)
        # Tính tổng của tất cả các số duy nhất trong mảng
        sum_unique = sum(set(nums))
        # Số cần tìm là 2 lần tổng của các số duy nhất trừ đi tổng của tất cả các số
        return 2 * sum_unique - sum_all
    
    
# Ví dụ sử dụng:
nums = [4, 1, 2, 1, 2]
solution = Solution()

print(solution.singleNumber(nums))  # Output: 4
