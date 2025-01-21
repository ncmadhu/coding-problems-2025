# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def build_linked_list(self, values):
        head = curr_node = None
        for value in values:
            new_node = ListNode(value)
            if not head:
                head = new_node
                curr_node = new_node
            else:
                curr_node.next = new_node
                curr_node = new_node
        # self.print_linked_list(head)
        return head

    def print_linked_list(self, linked_list):
        while linked_list:
            print(linked_list.val)
            linked_list = linked_list.next

    def merge_two_sorted_linked_list(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        curr_node = merged_list
        while list1 and list2:
            if list1.val <= list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            curr_node = curr_node.next
        if list1:
            curr_node.next = list1

        if list2:
            curr_node.next = list2

        return merged_list.next


if __name__ == "__main__":
    solution = Solution()
    # list1 = solution.build_linked_list([3,4,5])
    # list2 = solution.build_linked_list([1,3,5])
    # merged_list = solution.merge_two_sorted_linked_list(list1, list2)
    # solution.print_linked_list(merged_list)
    list1 = solution.build_linked_list([-9,3])
    list2 = solution.build_linked_list([5,7])
    merged_list = solution.merge_two_sorted_linked_list(list1, list2)
    solution.print_linked_list(merged_list)

