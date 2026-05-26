
def Solution(arr1, arr2):
    result = list(set(arr1) & set(arr2))
    
    return result


arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6]

print(Solution(arr1, arr2))