class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #this is a topo sort question
        #where we need to take courses in a specific order
        #unless there is a loop, then we can't complete the courses

        #soooo let's start first by creating the adj list to represent the graph
        adjList = collections.defaultdict(list)

        for preq,course in prerequisites:
            adjList[course].append(preq)

        #now that we have our graph represented, lets do some dfs, and keep track of the nodes that we are 
        #visiting in order to see whether we have a loop

        visiting = set()

        def dfs(node):

            if node in visiting: #loop was detected oh no
                return False
            if adjList[node] == []: # no prerequisites, we can complete this
                return True

            visiting.add(node)

            for preq in adjList[node]:
                if not dfs(preq):
                    return False
            visiting.remove(node)
            adjList[node] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

            
            

        
        