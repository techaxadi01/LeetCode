# LeetCode 171: Excel Sheet Column Number
# Approach: Base-26 Conversion | Time: O(n) | Space: O(1)

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        # Treat title as a base-26 number (A=1, B=2, ..., Z=26)
        for ch in columnTitle:
            result *= 26
            result += ord(ch) - ord('A') + 1

        return result
