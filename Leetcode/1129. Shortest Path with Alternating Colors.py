"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.
You are given two arrays redEdges and blueEdges where:
redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

Example 1:
Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
"""
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """
        1. Create an adjacency list contains neighbor node and color, 0 for red and the number 1 for blue.
        2. Create a answer array with the value -1 where answer[i] is the answer for the ith
        3. Create a 2D visit array in which visit[node][color] indicates whether node has yet been visited using an edge of color
        4. Create a queue, save 3 things:
        a) the current node, 
        b) the steps taken to visit the node, 
        c) the color of the previous edge used. 
        5. While the queue is not empty:
        + Remove the first element out of the queue to obtain [node, steps, prevColor].
        + Loop through all (neighbor, color) pairs in adj[node]. If a neighbor has not yet been visited with a color edge and
        color!=prevColor, we visit neighbor with the color edge by pushing [neighbor, steps + 1, color] in the queue.
        If this is neighbor's first visit, i.e., answer[neighbor] == -1, we set answer[neighbor] = steps + 1.
        Time: O(node + red + blue)
        Space: O(node + red + blue)
        """
        adj_red = defaultdict(list)
        adj_blue = defaultdict(list)
        for (a, b) in redEdges:
            adj_red[a].append(b)
        for (u, v) in blueEdges:
            adj_blue[u].append(v)
        dq = deque()
        visited = set()
        dq.append((0, 0, 0)) 
        dq.append((0, 0, 1)) 
        visited.add((0, 0))
        visited.add((0, 1))
        ans = [-1 for i in range(n)]
        while dq:
            u, step, col = dq.popleft()
            if ans[u] == -1:
                ans[u] = step
            if col == 0: #red
                for v in adj_blue[u]:
                    if (v, 1) not in visited:
                        visited.add((v, 1))
                        dq.append((v, step + 1, 1))
            else: #blue
                for v in adj_red[u]:
                    if (v, 0) not in visited:
                        visited.add((v, 0))
                        dq.append((v, step + 1, 0))
        return ans




        
