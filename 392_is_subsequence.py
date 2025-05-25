class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        
        i = 0
        j = 0
        
        while (j < len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(s)


s = "b"
t = "abc"
sol = Solution()
print(sol.isSubsequence(s,t))