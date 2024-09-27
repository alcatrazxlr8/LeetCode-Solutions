class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqMap = {}
        ans = []
        for i in range(numCourses):
            reqMap[i] = []
            
        for crs, req in prerequisites:
            reqMap[crs].append(req)
            
        visited = set()
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for req in reqMap[crs]:
                if not dfs(req):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            ans.append(crs)
            # reqMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return ans