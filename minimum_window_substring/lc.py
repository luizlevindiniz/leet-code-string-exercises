class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        letters_in_t: dict = {}
        letters_in_s: dict = {}

        start = 0

        ans = [-1, -1]
        len_of_ans = 10**6

        # edge case
        if m > n:
            return ""

        # counting letters in t
        for letter in t:
            letters_in_t[letter] = 1 + letters_in_t.get(letter, 0)

        have = 0
        need = sum(letters_in_t.values())

        # loop in s
        for end in range(0, n):
            letter = s[end]
            if letter in letters_in_t:
                letters_in_s[letter] = 1 + letters_in_s.get(letter, 0)

                if letters_in_s[letter] <= letters_in_t[letter]:
                    have += 1

            while have == need:
                if end - start + 1 < len_of_ans:
                    ans = [start, end]
                    len_of_ans = end - start + 1
                letter = s[start]
                if letter in letters_in_s:
                    if letters_in_s[letter] == letters_in_t[letter]:
                        have -= 1
                    letters_in_s[letter] -= 1

                start += 1

        return "" if ans == [-1, -1] else s[ans[0] : ans[1] + 1]


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("bbaa", "aba"))
