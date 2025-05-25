class Solution:
    def reverseWords(self, s: str) -> str:
        
        l = s.split()
        l.reverse()

        return ' '.join(l)
    
sol = Solution()
print(sol.reverseWords("  hello  world  "))