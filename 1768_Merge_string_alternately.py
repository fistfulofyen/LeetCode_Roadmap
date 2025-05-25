class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        len_w1 = len(word1)
        len_w2 = len(word2)

        smaller = min(len_w1,len_w2)

        merged = []
        for i in range(smaller):
            merged.append(word1[i])
            merged.append(word2[i])
        
        if len_w1 > len_w2:
            merged.append(word1[smaller:])
        else:
            merged.append(word2[smaller:])

        return ''.join(merged)

def main():
    solution = Solution()
    print(solution.mergeAlternately("abc", "pqrstu"))  # Output: "apbqcrstu"
    print(solution.mergeAlternately("ab", "pqrs"))     # Output: "apbqrs"

if __name__ == "__main__":
    main()