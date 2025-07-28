class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        visited = set()
        visiting = set()
        
        path = []
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)

            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False

            visited.add(course)
            visiting.remove(course)
            path.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return path
            
