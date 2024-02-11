from typing import List


class Solution:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    prime_numbers = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
    ]
    letters_to_prime_numbers = dict(zip(alphabet, prime_numbers))

    def word_to_prime_multiple(self, word: str) -> int:
        number = 1
        for letter in word:
            number *= self.letters_to_prime_numbers[letter]

        return number

    # O(n*m) time complexity
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # edge case
        if len(strs) == 1:
            return [strs]

        prime_numbers = {}

        for word in strs:
            prime_multiple = self.word_to_prime_multiple(word)
            if prime_multiple in prime_numbers:
                prime_numbers[prime_multiple].append(word)
            else:
                prime_numbers[prime_multiple] = [word]

        return list(prime_numbers.values())
