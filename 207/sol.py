import collections
lass Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = collections.defaultdict(int)
        outdegree = collections.defaultdict(list)
        for ele in prerequisites:
            indegree[ele[1]] += 1
            outdegree[ele[0]].append(ele[1])
        q = collections.deque()
        count = 0
        for i in range(numCourses):
            if i not in indegree:
                q.append(i)
                count += 1
        while q:
            head = q.popleft()
            for point in outdegree[head]:
                indegree[point] -= 1
                if indegree[point] == 0:
                    q.append(point)
                    count += 1
        if count == numCourses:
            return True
        else:
            return False