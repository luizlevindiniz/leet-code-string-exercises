from typing import List


class Solution:
    # O(n log n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers_seen_and_frequency = {}
        for num in nums:
            if num in numbers_seen_and_frequency:
                numbers_seen_and_frequency[num] += 1
            else:
                numbers_seen_and_frequency[num] = 1

        sorted_list = (
            sorted(
                numbers_seen_and_frequency.items(),
                key=lambda item: item[1],
                reverse=True,
            )
        )[:k]

        return [x[0] for x in sorted_list]
