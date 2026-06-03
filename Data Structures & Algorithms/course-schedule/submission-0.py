class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #this is essentially a graph question
        #adjacency list
        #the question is really asking: is there a path from node 1 to node n?

        #first step: lets form the adj list

        adjList = {i:[] for i in range(numCourses)} #list comprehensio
        for desired, prereq in prerequisites:
            adjList[prereq].append(desired)
        visit = set()

        #count paths by doing dfs backtracking

        def dfs(node):
            if node in visit: #loop is detected
                return False
            if adjList[node] == []: # no preq, so we good
                return True

            visit.add(node)
            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False
            visit.remove(node)
            adjList[node] = [] #optimization, if we need to dfs this node again, we know that its vistable already
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        
        