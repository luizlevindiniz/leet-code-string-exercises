class Solution:

    def get_elements_to_swap(self, seen: dict) -> int:
        max_occurr_seen = max(seen.values())
        sum_of_occurr = sum(seen.values())

        return sum_of_occurr - max_occurr_seen

    def characterReplacement(self, s: str, k: int) -> int:
        max_so_far = 0

        counter = 0
        seen: dict = {}

        i = 0
        for j in range(0, len(s)):
            # storing letter in seen
            seen[s[j]] = 1 + seen.get(s[j], 0)

            counter += 1
            elements_to_swap = self.get_elements_to_swap(seen=seen)

            if elements_to_swap > k:
                seen[s[i]] -= 1
                counter -= 1
                i += 1
            else:
                max_so_far = max(max_so_far, counter)

        return max_so_far


if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement("AABABBA", 1))
