class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we make adj list with courses and then run dfs starting from each node and maintaining a
        # visited till we get a case where we are able to reach all nodes
        # in the end we also check for courses that are not constrained (they will be true no matter what)
        reqMap = {}
        for i in range(numCourses):
            reqMap[i] = []
            
        for crs, req in prerequisites:
            reqMap[crs].append(req)
            
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if reqMap[crs] == []:
                return True
            visited.add(crs)
            for req in reqMap[crs]:
                if not dfs(req):
                    return False
            visited.remove(crs)
            reqMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
                