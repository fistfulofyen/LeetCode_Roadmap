
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # find vowels
        s = list(s)
        vowels = []
        for i in range(len(s)):
            if s[i] in ('a','e','i','o','u','A','E','I','O','U'):
                vowels.append(s[i])
                s[i] = None
        
        vowels.reverse()
        j = 0
        for i in range(len(s)):
            if s[i] is None:
                s[i] = vowels[j]
                j += 1

        return ''.join(s)

s = "leetcode"

sol = Solution()
print(sol.reverseVowels(s))
