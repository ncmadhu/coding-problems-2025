# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

def merge_two_sorted_lists(list1, list2):
    merged_list = []
    while list1  and list2:
        if list1[0] <= list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))

    while list1:
        merged_list.append(list1.pop())
    while list2:
        merged_list.append(list2.pop())
    return merged_list


if __name__ == "__main__":
    print(merge_two_sorted_lists([1,2,4], [1,3,4]))
    print(merge_two_sorted_lists([], []))
    print(merge_two_sorted_lists([], [0]))
