"""
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
"""

def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        For each edge (u, v), traverse the graph by DFS to check can go from u to v or not. 
        If yes, it can be a duplicate edge
        Time: O(n^2) with n is num of vertices
        Space: O(n) because of construction graph
        """

        def dfs(graph, start, end, used):
            if start not in used:
                used.add(start)
                if start == end:
                    return True
                for ne in graph[start]:
                    if dfs(graph, ne, end, used): 
                        return True
        
        def helper(edges): 
            graph = collections.defaultdict(set)
            for u, v in edges:
                used = set()
                if u in graph and v in graph and dfs(graph, u, v, used):
                        return u, v
                graph[u].add(v)
                graph[v].add(u)
                
        return helper(edges)
