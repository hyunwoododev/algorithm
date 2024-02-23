# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left,right=1,n
        while left<=right:
            mid=(right+left)//2
            num=(mid/2)*(mid+1)
            if num<=n:
                left=mid+1
            else:
                right=mid-1
        return right

