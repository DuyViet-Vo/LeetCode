class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Chuyển chuỗi nhị phân thành số nguyên
        int_a = int(a, 2)
        int_b = int(b, 2)
        
        # Thực hiện phép cộng
        result = int_a + int_b
        
        # Chuyển kết quả trở lại thành chuỗi nhị phân
        return bin(result)[2:]

a = "1010"
b = "1011"
solution = Solution()
result = solution.addBinary(a,b)
print(result)