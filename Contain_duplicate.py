
def Solution(nums):

    if len(nums) != len(set(nums)):
        return True
    return False



nums = [1,2,3,1]
print(Solution(nums))