from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    planted += 1
        return planted >= n


if __name__ == "__main__":
    sol = Solution()
    # print(sol.canPlaceFlowers([1,0,0,0,1], 1))
    # print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))
    # print(sol.canPlaceFlowers([1,0,0,0,0,1], 2))
    # print(sol.canPlaceFlowers([0], 1))
    # print(sol.canPlaceFlowers([0, 0, 1, 0, 1], 1))
    # print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 1))
    print(sol.canPlaceFlowers([0,1,0,1,0,1,0,0], 1))