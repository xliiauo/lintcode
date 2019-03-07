import math
import ipdb


def minimumTotal(triangle):
  f = {}
  f[(0, 0)] = triangle[0][0]

  for i in range(1, len(triangle)):

    for j in range(0, i + 1):
      f[(i, j)] = math.inf
      if f.get((i - 1, j)) is not None:
        f[(i, j)] = min(f[(i, j)], f[(i - 1, j)])
      if f.get((i - 1, j - 1)) is not None:
        f[(i, j)] = min(f[(i, j)], f[(i - 1, j - 1)])
      f[(i, j)] += triangle[i][j]

  rst = []
  for i in range(0, len(triangle)):
    rst.append(f[(len(triangle) - 1, i)])
  return min(rst)

print(minimumTotal(
[[-2],[5,2],[-3,2,7],[8,7,2,-8],[7,5,3,8,-1],[-7,-2,-2,0,-1,6],[4,7,7,-9,9,8,2],[-5,-8,-1,-1,6,7,3,-5],[4,1,-8,-7,-1,5,7,-8,3],[-7,-8,-8,0,1,-3,-4,-8,-6,9],[-7,-9,5,1,-8,6,9,0,-1,6,9],[0,-3,-3,-2,-1,6,-7,-7,4,3,-5,2]]))
