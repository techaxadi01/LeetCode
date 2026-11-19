# LeetCode 29: Divide Two Integers
# Approach: Exponential Search / Doubling | Time: O((log(dividend))^2) | Space: O(1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle 32-bit signed integer overflow edge case
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine result sign
        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        a, b = abs(dividend), abs(divisor)
        ans = 0

        # Subtract largest power-of-two multiples of divisor
        while a >= b:
            temp = b
            count = 1

            # Double divisor until it exceeds remaining dividend
            while a >= temp + temp:
                temp = temp + temp
                count = count + count

            a -= temp
            ans += count

        return -ans if sign < 0 else ans


"""
Alternative Approach (Bit Manipulation / Bit Shifts):
Time: O(32) = O(1) | Space: O(1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = -1 if (dividend < 0) != (divisor < 0) else 1
        a, b = abs(dividend), abs(divisor)
        ans = 0

        for i in range(31, -1, -1):
            if (a >> i) >= b:
                ans += 1 << i
                a -= b << i

        return -ans if sign < 0 else ans
"""
