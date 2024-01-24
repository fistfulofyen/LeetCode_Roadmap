import unittest

def is_valid(s):
    if len(s) % 2 != 0: return False

    stack = []
    para = {"}": "{",
            ")": "(",
            "]": "["}
    
    for close in s:
        if close in para:
            if stack and stack[-1] == para[close]:
                stack.pop()
            else:
                return False
        else:
            stack.append(close)

    return True if not stack else False


class TestIsValid(unittest.TestCase):
    def test_valid_strings(self):
        self.assertTrue(is_valid("()"))
        self.assertTrue(is_valid("()[]{}"))
        self.assertTrue(is_valid("{[()]}"))

    def test_invalid_strings(self):
        self.assertFalse(is_valid("(]"))
        self.assertFalse(is_valid("([)]"))
        self.assertFalse(is_valid("]"))

    def test_empty_string(self):
        self.assertTrue(is_valid(""))

    def test_mixed_characters(self):
        self.assertFalse(is_valid("(a+b)*c"))
        self.assertFalse(is_valid("abc(def)"))

if __name__ == '__main__':
    unittest.main()
