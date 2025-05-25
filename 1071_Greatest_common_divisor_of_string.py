import math

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2 = len(str1), len(str2)
        gcd = math.gcd(len1,len2)
        candidate = str1[:gcd]
        
        # Check if both strings are formed by repeating the candidate
        if str1 == candidate * (len1 // gcd) and str2 == candidate * (len2 // gcd):
            return candidate

        return ""


def main():
    str1 = "ABCABC"
    str2 = "ABC"
    str3 = "ABABAB"
    str4 = "ABAB"
    str5 = "LEET"
    str6 = "CODE"
    s = Solution()
    print(s.gcdOfStrings(str1,str2))
    print(s.gcdOfStrings(str3,str4))
    print(s.gcdOfStrings(str5,str6))

if __name__ == "__main__":
    main()