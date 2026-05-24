
def Solution(nums):

    if len(nums) != len(set(nums)):
        return True
    return False



nums = [1,2,3,1]
print(Solution(nums))


# Different way

def Solution(nums):

    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False        


nums = [1,2,3,4,1]
print(Solution(nums))