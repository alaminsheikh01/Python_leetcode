

def majorityElement(nums):
    count = 0
    candit = 0
    
    for num in nums:
        if count == 0:
            candit = num
            
        if num == candit:
            count +=1
        else:
            count -=1
            
    return candit                
    


nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))