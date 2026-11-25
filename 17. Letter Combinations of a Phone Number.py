# LeetCode 17: Letter Combinations of a Phone Number
# Approach: Iterative (BFS / Cartesian Product) | Time: O(4^n * n) | Space: O(4^n * n)

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        res = [""]

        # Expand combinations digit by digit
        for digit in digits:
            temp = []
            for combo in res:
                for ch in phone[digit]:
                    temp.append(combo + ch)
            res = temp

        return res
