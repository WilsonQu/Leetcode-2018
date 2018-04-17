# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        q = collections.deque()
        q.append(node)
        re = UndirectedGraphNode(node.label)
        track = {node.label:re}
        visited = {node.label}
        while q:
            head = q.popleft()
            for neighbornode in head.neighbors:
                track[neighbornode.label] = track.get(neighbornode.label, UndirectedGraphNode(neighbornode.label))
                track[head.label].neighbors.append(track[neighbornode.label])
                if neighbornode.label not in visited:
                    q.append(neighbornode)
                    visited.add(neighbornode.label)
        return re