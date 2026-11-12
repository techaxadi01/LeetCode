# LeetCode 172: Factorial Trailing Zeroes
# Approach: Math (Counting Factors of 5) | Time: O(log5(n)) | Space: O(1)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero = 0

        # Trailing zeroes come from 10 (2 * 5); count multiples of 5, 25, 125, ...
        while n > 0:
            zero += n // 5
            n //= 5

        return zero
