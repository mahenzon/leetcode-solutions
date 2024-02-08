class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        num = x
        while num:
            rev = rev * 10 + num % 10
            num //= 10

        return rev == x
