# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Hàm để chuyển danh sách liên kết sang danh sách
        def list_to_array(node):
            array = []
            while node:
                array.append(node.val)
                node = node.next
            return array

        # Hàm để chuyển danh sách thành danh sách liên kết
        def array_to_list(array):
            dummy = ListNode()
            current = dummy
            for value in array:
                current.next = ListNode(value)
                current = current.next
            return dummy.next

        # Chuyển danh sách liên kết thành danh sách
        array1 = list_to_array(list1)
        array2 = list_to_array(list2)

        # Sắp xếp các danh sách
        merged_array = sorted(array1 + array2)

        # Chuyển danh sách thành danh sách liên kết và trả về
        merged_list = array_to_list(merged_array)
        return merged_list

# Test với hai danh sách liên kết
list1 = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
list2 = ListNode(1, ListNode(3, ListNode(4)))

solution = Solution()
result = solution.mergeTwoLists(list1, list2)

# In kết quả
while result:
    print(result.val, end=" ")
    result = result.next
