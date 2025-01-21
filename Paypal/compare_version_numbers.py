# Example 1:
# Input: version1 = "1.2", version2 = "1.10"
# Output: -1
# Explanation:
# version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.
#
# Example 2:
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation:
# Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
#
# Example 3:
# Input: version1 = "1.0", version2 = "1.0.0.0"
# Output: 0
# Explanation:
# version1 has less revisions, which means every missing revision are treated as "0".

def compare_version_numbers(version1, version2):
    v1 = [int(x) for x in version1.split('.')]
    v2 = [int(x) for x in version2.split('.')]
    i = j = 0
    while i < len(v1) and j < len(v2):
        if v1[i] < v2[i]:
            return -1
        elif v1[i] > v2[i]:
            return 1
        i += 1
        j += 1
    while j < len(v2):
        if v2[j] > 0:
            return -1
        j += 1
    while i < len(v1):
        if v1[i] > 0:
            return 1
        i += 1
    return 0


def alternate_solution_1(version1, version2):

    def get_next_chunk(v, p, n):
        if p > n - 1:
            return 0, p
        p_end = p
        while p_end < n and v[p_end] != '.':
            p_end += 1
        return int(v[p:p_end]), p_end + 1

    p1 = p2 = 0
    n1 = len(version1)
    n2 = len(version2)

    while p1 < n1 or p2 < n2:
        i1, p1 = get_next_chunk(version1, p1, n1)
        i2, p2 = get_next_chunk(version2, p2, n2)
        if i1 > i2:
            return 1
        elif i1 < i2:
            return -1
    return 0




if __name__ == "__main__":
    print(alternate_solution_1("1.0", "1.0.0.0"))
    # print(compare_version_numbers("1.2", "1.10"))
    # print(compare_version_numbers("1.01", "1.001"))
    # print(compare_version_numbers("1.0", "1.0.0.0"))
