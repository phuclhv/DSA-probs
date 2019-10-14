'''
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. 
Other areas are safe to sail in. There are other explorers trying to find the treasure. 
So you must figure out a shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters. 
You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. 
The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D.
 You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in.
 Output the minimum number of steps to get to any of the treasure islands.

Example:

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
'''
from collections import deque
def shortest_path(grid):
  if len(grid) == 0 or len(grid[0]) == 0:
    return None
  
  nrow, ncol = len(grid), len(grid[0])
  sources = deque()
  min_step = float("inf")

  for row in range(0, nrow):
    for col in range(0, ncol):
      if grid[row][col] == 'S':
        sources.append((row,col))

  def shotest_path_from(start_x, start_y):
    matrix = grid
    visited = deque([((start_x,start_y),0)])
    matrix[start_x][start_y] = 'D'
    while visited:      
      (x,y), step = visited.popleft()
      for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if 0 <= x + dx < nrow and 0 <= y + dy < ncol:
          if matrix[x + dx][y + dy] == 'X':
            return step + 1
          if matrix[x + dx][y + dy] == 'O':
            matrix[x + dx][y + dy] = 'D'
            visited.append(((x + dx,y + dy), step+1))
    return float("inf")

        
  while sources:
    (source_x, source_y) = sources.popleft()
    min_step = min(shotest_path_from(source_x, source_y), min_step)
  
  return min_step
  
island = [['S', 'O', 'O', 'S', 'S'], ['D', 'O', 'D', 'O', 'D'], ['O', 'O', 'O', 'O', 'X'], ['X', 'D', 'D', 'O', 'O'], ['X', 'D', 'D', 'D', 'O']]
print(shortest_path(island))