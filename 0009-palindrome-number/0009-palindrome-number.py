class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        number = x
        reversed_number = 0
        while number:
            reversed_number = reversed_number * 10 + number % 10
            number //= 10
        
        return reversed_number == x