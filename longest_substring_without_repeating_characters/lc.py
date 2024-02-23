class Solution:
    # refactoring - sliding window O(n) solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        startWindow = 0

        for endWindow in range(0, len(s)):
            if s[endWindow] not in seen:
                seen.add(s[endWindow])
                max_len = max(max_len, endWindow - startWindow + 1)
            else:
                while s[startWindow] != s[endWindow]:
                    seen.remove(s[startWindow])
                    startWindow += 1
                startWindow += 1

        return max_len

    """
    # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        seen = {}
        max_range = 0
        sequence_range = 0

        for i in range(0, len(s)):
            if s[i] not in seen:
                seen[s[i]] = i

            else:
                sequence_range = max(sequence_range, i - start)

                start = max(start, seen[s[i]] + 1)
                seen[s[i]] = i

            max_range = max(max_range, sequence_range, i - start + 1)

        return max_range
    """


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("tmmzuxt"))
