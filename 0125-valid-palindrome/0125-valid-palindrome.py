class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet ='abcdefghijklmnopqrstuvwxyz1234567890'
        s=s.lower()
        for a in s:
            if a not in alphabet:
                s=s.replace(a,'')
        
        if s==s[-1::-1]:
            return True
        else:
            return False
                
        