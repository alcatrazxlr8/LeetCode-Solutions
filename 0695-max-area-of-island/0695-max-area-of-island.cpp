#include <vector>
class Solution {
public:
    int dfs(vector<vector<int>>& grid, int x, int y){
        if(x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size() || grid[x][y] == 0){
            return 0;
        }
        grid[x][y] = 0;
        return 1 + dfs(grid, x-1, y) + dfs(grid, x, y-1) + dfs(grid, x+1, y) + dfs(grid, x, y+1);
        
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxIslandArea = 0;
        int m = grid.size();
        int n = grid[0].size();

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if (grid[i][j] == 1){
                    maxIslandArea = max(maxIslandArea, dfs(grid, i, j));
                }
            }
        }
        return maxIslandArea;
    }
};