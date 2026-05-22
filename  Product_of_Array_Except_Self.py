class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        
        # create array with 1
        answer = [1] * n

        # Left products
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # Right products
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
    



nums = [1, 2, 3, 4]
sol = Solution()
print(sol.productExceptSelf(nums))