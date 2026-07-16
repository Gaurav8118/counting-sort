from collections import Counter

class Solution:
    def smallestPalindrome(self, s):   # <-- match the driver call
        freq = Counter(s)
        half = []
        middle = ""

        for ch in sorted(freq.keys()):
            count = freq[ch]
            half.extend([ch] * (count // 2))
            if count % 2 == 1:
                middle = ch

        first_half = "".join(half)
        second_half = first_half[::-1]
        return first_half + middle + second_half
