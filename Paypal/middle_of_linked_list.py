class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def build_linked_list(nums):
    head = prev = None
    for n in nums:
        new_node = ListNode(n)
        if not head:
             head = new_node
             prev =  head
        else:
            prev.next = new_node
            prev = new_node
    return head


def get_linked_list(start):
    curr = start
    nums = []
    while curr:
        nums.append(curr.val)
        curr = curr.next
    return nums

def middle_of_linked_list(head):
    fast = slow = head
    while fast and fast.next:
        slow =  slow.next
        fast = fast.next.next
    return slow.val


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    print(get_linked_list(head))
    print(middle_of_linked_list(head))
