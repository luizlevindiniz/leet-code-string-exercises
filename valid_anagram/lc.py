class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        if len(s) != len(t):
            return False

        letters_in_first_string: dict = {}
        for letter in s:
            if letter in letters_in_first_string:
                letters_in_first_string[letter] += 1
            else:
                letters_in_first_string[letter] = 1

        for letter in t:
            if (
                letter in letters_in_first_string
                and letters_in_first_string[letter] > 0
            ):
                letters_in_first_string[letter] -= 1
            else:
                return False

        return True
