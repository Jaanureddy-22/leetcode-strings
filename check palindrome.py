def isPalindrome(s):
    #code here
    val=s[::-1]
    if s.upper() == val.upper():
        return True
    return False
    