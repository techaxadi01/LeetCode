# LeetCode 2747: Count Zero Request Servers
# Approach: Sliding Window + Sorting | Time: O(L log L + Q log Q) | Space: O(n + Q)

class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        # Sort logs by timestamp and queries by time while preserving original index
        logs.sort(key=lambda a: a[1])
        sorted_q = sorted((q, i) for i, q in enumerate(queries))

        ans = [0] * len(queries)
        active = [0] * (n + 1)    # Request frequency per server in current window
        left = right = count = 0  # count tracks number of unique active servers

        for q, idx in sorted_q:
            # Expand window: include logs up to query time q
            while right < len(logs) and logs[right][1] <= q:
                s = logs[right][0]
                if active[s] == 0:
                    count += 1
                active[s] += 1
                right += 1

            # Shrink window: remove logs before (q - x)
            while left < right and logs[left][1] < q - x:
                s = logs[left][0]
                active[s] -= 1
                if active[s] == 0:
                    count -= 1
                left += 1

            # Inactive servers = total servers - active servers
            ans[idx] = n - count

        return ans
