def longest_common_prefix(strs):
    if not strs:
        return ""

    # Sắp xếp danh sách theo thứ tự từ điển để đảm bảo các chuỗi giống nhau sẽ được đặt cùng nhau
    strs.sort()

    # Lấy chuỗi đầu tiên và cuối cùng sau khi sắp xếp
    first_str = strs[0]
    last_str = strs[-1]

    # Tìm độ dài của đầu chung
    common_length = 0
    for i in range(min(len(first_str), len(last_str))):
        if first_str[i] == last_str[i]:
            common_length += 1
        else:
            break

    # Trả về đầu chung
    return first_str[:common_length]

# Test với đầu vào ["flower","flow","flight"]
strs = ["flower","flow","flight"]
result = longest_common_prefix(strs)
print(result)
