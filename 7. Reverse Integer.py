# LeetCode 7: Reverse Integer
# Approach: Math / Digit Extraction | Time: O(log|x|) | Space: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        # 32-bit signed integer range
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        result = 0
        x = abs(x)

        # Extract digits from right to left and append to result
        while x > 0:
            result = (result * 10) + (x % 10)
            x //= 10

        result *= sign

        # Return 0 if reversed integer overflows 32-bit range
        if not (INT_MIN <= result <= INT_MAX):
            return 0

        return result

"""
Another approach using string manipulation:
class Solution:
    def reverse(self, x: int) -> int:
        # 32-bit signed integer range
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        x_rev = str(x)[::-1]
        result = int(x_rev)

        result *= sign

        # Return 0 if reversed integer overflows 32-bit range
        if not (INT_MIN <= result <= INT_MAX):
            return 0

        return result
"""