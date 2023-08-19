class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, k: int) -> int:
        if N <= 0:
            return 0
        if not times and N > 1:
            return -1
        gr = collections.defaultdict(list)
        for u, v, w in times:
            gr[u].append((v, w))
        dist = [float("inf")] * (N + 1)
        dist[k] = 0
        used = [False] * (N + 1)
        pool = [(0, k)]
        while pool:
            cur_cost, cur_node = heapq.heappop(pool)
            used[cur_node] = True
            for ch, cost in gr[cur_node]:
                if not used[ch] and dist[ch] > dist[cur_node] + cost:
                    dist[ch] = dist[cur_node] + cost
                    heapq.heappush(pool, (dist[ch], ch))

        ans = max(dist[1:])
        return ans if ans < float("inf") else -1