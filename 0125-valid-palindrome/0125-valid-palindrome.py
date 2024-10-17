class Solution:
    def isPalindrome(self, string: str) -> bool:
        string = string.lower()

        left, right = 0, len(string) - 1

        while left <= right:
            if string[left].isalnum() and string[right].isalnum():
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            else:
                if not string[left].isalnum():
                    left += 1
                elif not string[right].isalnum():
                    right -= 1

        return True