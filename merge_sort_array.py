from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Không cần trả về bất kỳ điều gì, chỉ cần sửa đổi nums1 trong chính nó.
        """
        # Khởi tạo con trỏ cho nums1 và nums2
        p1 = m - 1
        p2 = n - 1
        # Khởi tạo con trỏ cho cuối của nums1 đã được gộp
        p = m + n - 1
        
        # Gộp nums1 và nums2 từ cuối
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # Nếu còn phần tử trong nums2, sao chép chúng vào nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]

# Ví dụ minh họa
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)
print("Mảng đã gộp:", nums1)
