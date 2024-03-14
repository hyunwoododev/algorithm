# https://leetcode.com/problems/product-of-array-except-self/description/

# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftRes = [1]*len(nums)
        rightRes =[1]*len(nums)

        for i in range(1,len(nums)):
            leftRes[i] = leftRes[i-1] * nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            rightRes[j] = rightRes[j+1] * nums[j+1]
        
        answer = []
        for i in range(len(nums)):
            answer.append(leftRes[i] * rightRes[i])
            
        return answer