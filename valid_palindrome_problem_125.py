class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if ord(char)>=65 and ord(char) <=90:
                val = ord(char) + 32
                new_s = new_s + chr(val)
            elif ord(char)>=97 and ord(char)<=122:
                new_s = new_s + char
            elif ord(char)>=48 and ord(char)<=57:
                new_s = new_s + char
        print(new_s)
        if new_s == new_s[::-1]:
            return True
        else:
            return False
        