def is_palindrome(num):
    # Chuyển số thành chuỗi để dễ kiểm tra đối xứng
    str_num = str(num)
    
    # So sánh chuỗi với chuỗi đảo ngược
    return str_num == str_num[::-1]

# Nhập số từ người dùng
number = int(input("Nhập một số: "))

# Kiểm tra xem số có phải là số palindrome hay không
if is_palindrome(number):
    print(f"{number} là số palindrome.")
else:
    print(f"{number} không phải là số palindrome.")