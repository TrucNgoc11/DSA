class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        """
        sort to make sure all the query that have s1 <= s2
        some exclude case that s1 == s2 or heights[s1] < heights[s2] => update s2 to ans
        Sort the remaining queries by b, decrease
        For each b, update the stack so it contains increasing heights for range (b, n)
        binary_search for the first height larger than s1
        """
        n = len(heights)
        ans = [0] * len(queries)
        tmp = []
        for idx, q in enumerate(queries):
            s1, s2 = sorted(q)
            if s1 == s2 or heights[s1] < heights[s2]:
                ans[idx] = s2
            else:
                tmp.append((s1, s2, idx))
        j, queue = n - 1, deque()
        for s1, s2, i in sorted(tmp, key=itemgetter(1), reverse=True): #the same as lambda
            while j > s2:
                while queue and heights[queue[0]] < heights[j]:
                    queue.popleft()
                queue.appendleft(j)
                j -= 1
            #print(queue)
            k = bisect_right(queue, heights[s1], key=lambda x: heights[x])
            ans[i] = -1 if k == len(queue) else queue[k]
        return ans
            
        


  
    

                

