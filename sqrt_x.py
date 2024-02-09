class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # Khi vòng lặp kết thúc, right sẽ là giá trị làm tròn xuống của căn bậc hai

x = 8
solution = Solution()
resulf = solution.mySqrt(x)
print(resulf)