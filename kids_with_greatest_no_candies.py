from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List:
        result = [False for x in range(len(candies))]
        max_candy = max(candies)
        result[0] = True
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= max_candy:
                result[i] = True
        return result



if __name__ == "__main__":
    sol = Solution()
    print(sol.kidsWithCandies([2,3,5,1,3], 3))
    print(sol.kidsWithCandies([4,2,1,1,2], 1))
    print(sol.kidsWithCandies([12,1,12], 10))