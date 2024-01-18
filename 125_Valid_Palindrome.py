import unittest

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    new_string = ""
    for c in s:
        if c.isalnum():
            new_string += c.lower()
    return new_string == new_string[::-1]

def is_alnum(c):
    return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))

def isPalindrome_inplace(s):
    l, r = 0, len(s) -1

    while l < r:
        while l < r and not is_alnum(s[l]):
            l += 1
        while l < r and not is_alnum(s[r]):
            r -= 1    
        if s[l].lower() != s[r].lower():
            return False
        
        l, r = l + 1, r - 1

    return True


def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is a palindrome
    return cleaned_s == cleaned_s[::-1]

class TestIsPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(isPalindrome("A man, a plan, a canal, Panama"))

    def test_not_palindrome(self):
        self.assertFalse(isPalindrome("Hello, World!"))

    def test_empty_string(self):
        self.assertTrue(isPalindrome(""))

    def test_single_character(self):
        self.assertTrue(isPalindrome("a"))

    def test_whitespace_palindrome(self):
        self.assertTrue(isPalindrome("Able was I ere I saw Elba"))

if __name__ == '__main__':
    unittest.main()
