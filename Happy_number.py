
def isHappy(num):
    seen = set()
    
    while num != 1:
        if num in seen:
            return False
        
        seen.add(num)
        
        sum = 0
        
        while num > 0:
            digit = num % 10
            sum += digit ** 2
            num //= 10
            
        num = sum
    
    return True

input = 2
print(isHappy(input))