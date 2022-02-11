def numIslands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '0':  
                helper(grid, i, j)
                count += 1
    return count

def helper(grid, i, j):
    if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
        return
    if grid[i][j] == '0':
        return
    grid[i][j] = '0'
    helper(grid, i - 1, j)
    helper(grid, i + 1, j)
    helper(grid, i, j - 1)
    helper(grid, i, j + 1)      
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))