class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        letters_in_t: dict = {}
        start = 0
        substring_to_return = s
        hasChanged = False

        # edge case
        if m > n:
            return ""

        # counting letters in t
        for letter in t:
            letters_in_t[letter] = 1 + letters_in_t.get(letter, 0)

        # getting start position
        for letter in s:
            if letter not in letters_in_t:
                start += 1
            else:
                break

        # loop in s
        for end in range(start, n):
            if s[end] in letters_in_t:
                letters_in_t[s[end]] -= 1

            while all(x <= 0 for x in letters_in_t.values()) and start <= end:
                substring = s[start : end + 1]
                hasChanged = True
                if len(substring) < len(substring_to_return):
                    substring_to_return = substring
                if s[start] in letters_in_t:
                    letters_in_t[s[start]] += 1
                start += 1

        if hasChanged:
            return substring_to_return
        return ""


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("bcdefggg", "a"))
    print(s.minWindow("cabwefgewcwaefgcf", "cae"))
