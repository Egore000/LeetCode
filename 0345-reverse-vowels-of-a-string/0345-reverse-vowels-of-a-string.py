class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS_LETTERS = 'AaEeIiOoUu'
        s = list(s)
        
        vowels = []
        for i, char in enumerate(s):
            if char in VOWELS_LETTERS:
                vowels.append(char)
        
        vowels.reverse()
        j = 0
        for i, char in enumerate(s):
            if char in VOWELS_LETTERS:
                s[i] = vowels[j]
                j += 1
        
        return ''.join(s)
            
            

