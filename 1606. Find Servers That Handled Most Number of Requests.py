# LeetCode 1606: Find Servers That Handled Most Number of Requests
# Approach: Min-Heap + SortedList | Time: O(n log k) | Space: O(k)

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))  # Tracks available servers in sorted order
        busy = []                         # Min-heap of (end_time, server_id)
        count = [0] * k                   # Request count per server

        for i, (a, l) in enumerate(zip(arrival, load)):
            # Free up servers that finished their tasks by arrival time a
            while busy and busy[0][0] <= a:
                _, server = heappop(busy)
                available.add(server)

            # Drop request if all servers are busy
            if not available:
                continue

            # Find the first available server starting from (i % k)
            idx = available.bisect_left(i % k)
            if idx == len(available):
                idx = 0  # Wrap around to the lowest available server

            server = available.pop(idx)
            count[server] += 1
            heappush(busy, (a + l, server))

        mx = max(count)
        return [i for i, c in enumerate(count) if c == mx]
