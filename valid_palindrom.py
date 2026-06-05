
def Palindrome(s):
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left +=1
        while left < right and not s[right].isalnum():
            right -=1
        if s[left].lower() != s[right].lower():
            return False
        
        left +=1
        right -=1
               
    return True



s = "A man, a plan, a canal: Panama"
print(Palindrome(s))



# 125. Valid Palindrome
# in normal way without space and comma and case sensitive
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         left = 0
#         right = len(s) - 1

#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left +=1
#             right -=1
#         return True        