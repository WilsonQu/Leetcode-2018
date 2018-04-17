class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) == 0 and n == 1:
            return True
        dic = collections.defaultdict(list)
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
        if len(dic) != n:
            return False
        q = collections.deque()
        visited = {edges[0][0]}
        q.append((edges[0][0],None))
        while q:
            head = q.popleft()
            for neighbor in dic[head[0]]:
                if neighbor == head[1]:
                    continue
                if neighbor in visited:
                    return False
                q.append((neighbor,head[0]))
                visited.add(neighbor)
        if len(list(visited)) != n:
            return False
        return True
            
            
            
        