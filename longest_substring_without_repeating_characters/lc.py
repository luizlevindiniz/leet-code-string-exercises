class Solution:
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
