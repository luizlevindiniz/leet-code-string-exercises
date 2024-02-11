class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_str = "".join(char for char in s if char.isalnum()).lower()

        len_of_formatted_str = len(formatted_str)
        # edge case: empty string
        if len_of_formatted_str == 0:
            return True

        i = 0
        j = len_of_formatted_str - 1

        while i < j:
            if formatted_str[i] != formatted_str[j]:
                return False
            i += 1
            j -= 1

        return True
