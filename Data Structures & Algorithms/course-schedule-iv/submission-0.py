class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adjList = collections.defaultdict(list)
        prereqMap = {}

        for prereq, course in prerequisites:
            adjList[course].append(prereq)

        
        output = []
        preq = []

        def dfs(course):

            if course not in prereqMap:
                prereqMap[course] = set()
                for prereq in adjList[course]:
                    prereqMap[course] |= dfs(prereq) #union of hashset
                prereqMap[course].add(course)
            return prereqMap[course]
                

        for i in range(numCourses):
            dfs(i)

        for prereq, course in queries:
            if prereq in prereqMap[course]:
                output.append(True)
            else:
                output.append(False)
        
        return output

            

            
