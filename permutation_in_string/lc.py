class Solution:
    # O(n+m)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        seen_in_s1: dict = {}

        # populating s1 dict
        for letter in s1:
            seen_in_s1[letter] = 1 + seen_in_s1.get(letter, 0)

        copy_of_seen = seen_in_s1.copy()

        for idx, letter in enumerate(s2):
            if letter in copy_of_seen:
                copy_of_seen[letter] -= 1

                while copy_of_seen[letter] < 0:
                    i = s2[start]
                    copy_of_seen[i] += 1
                    start += 1
            else:
                copy_of_seen = seen_in_s1.copy()
                start = idx + 1

            if all(x == 0 for x in copy_of_seen.values()) and (idx - start + 1) == len(
                s1
            ):
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("hello", "ooolleoooleh"))
    print(s.checkInclusion("ab", "eidbaooo"))
    print(s.checkInclusion("adc", "dadc"))
