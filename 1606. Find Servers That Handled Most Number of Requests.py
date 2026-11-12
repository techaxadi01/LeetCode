# LeetCode 1606: Find Servers That Handled Most Number of Requests
# Approach: Two Min-Heaps (Available + Busy) | Time: O(n log k) | Space: O(k)

import heapq


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))  # Min-heap of available servers (shifted >= i)
        busy = []                   # Min-heap of (end_time, server_id)
        count = [0] * k             # Request count per server

        for i, (a, l) in enumerate(zip(arrival, load)):
            # Free up servers that finished their tasks by arrival time a
            while busy and busy[0][0] <= a:
                _, server = heapq.heappop(busy)
                # Shift ID into [i, i + k - 1] so min-heap picks next clockwise from i % k
                heapq.heappush(available, i + (server - i) % k)

            # Drop request if all servers are busy
            if not available:
                continue

            server = heapq.heappop(available) % k
            count[server] += 1
            heapq.heappush(busy, (a + l, server))

        mx = max(count)
        return [i for i, c in enumerate(count) if c == mx]
