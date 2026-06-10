class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #this is another topo sort question
        #where in the first question, we needed to return if there is a cycle detected
        #now, we need to return the topo sort instead

        #lets first start by building the adj list to represent the graph
        adjList = collections.defaultdict(list)

        for prereq, course in prerequisites:
            adjList[course].append(prereq)

        topSort = []
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if adjList[node] == []:
                topSort.append(node)
                return True
            
            visiting.add(node)

            for prereq in adjList[node]:
                if not dfs(prereq):
                    return False
            visiting.remove(node)
            adjList[node] = []
            topSort.append(node)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return topSort[::-1]

        