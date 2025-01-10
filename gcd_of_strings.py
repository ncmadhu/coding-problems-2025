class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        print(f"GCD of strings {str1} {str2}")
        # Get the smallest string of two as base
        len1, len2 = len(str1), len(str2)

        def valid(index):
            # Check if both the strings are divisible by the current base length
            if len1 % index or len2 % index:
                return False
            # get the multiplier for both the strings
            n1, n2 = len1 // index, len2 // index
            base = str1[:index]
            # check the strings get multiplied and are equal
            return str1 == n1 * base and str2 == n2 * base

       # Loop from back of the smallest string to get a common prefix
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return "None"


if __name__ == "__main__":
    sol = Solution()
    print(sol.gcdOfStrings("ABCABC", "ABC"))
    print(sol.gcdOfStrings("ABAB", "ABC"))
    print(sol.gcdOfStrings("ABABAB", "ABAB"))
    print(sol.gcdOfStrings("ABAB", "ABAB"))
