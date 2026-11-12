# LeetCode 168: Excel Sheet Column Title
# Approach: Base-26 Conversion | Time: O(log26(n)) | Space: O(log26(n))

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col = []

        while columnNumber > 0:
            columnNumber -= 1  # Shift 1-indexed (1..26) to 0-indexed (0..25)
            col.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26

        return "".join(col[::-1])  # Reverse digits collected from right to left
