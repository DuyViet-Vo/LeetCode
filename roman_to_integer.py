def roman_to_int(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    i = 0
    while i < len(roman):
        # Nếu ký tự tiếp theo lớn hơn ký tự hiện tại, thì trừ ký tự hiện tại
        if i + 1 < len(roman) and roman_numerals[roman[i]] < roman_numerals[roman[i + 1]]:
            result += roman_numerals[roman[i + 1]] - roman_numerals[roman[i]]
            i += 2  # Bước 2 vì chúng ta đã xử lý 2 ký tự
        else:
            result += roman_numerals[roman[i]]
            i += 1

    return result

# Thử nghiệm hàm với số La Mã
roman_number = "LVIII"
arabic_number = roman_to_int(roman_number)
print(f"Số thường tương ứng với số La Mã {roman_number}: {arabic_number}")
