grid_str = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 99 57 60 87 17 40 98 43 69 00 04 56 62 00
81 49 31 73 55 94 14 29 93 71 40 67 53 99 30 99 49 13 36 65
52 70 95 23 99 60 11 42 69 24 68 56 01 32 99 98 37 02 36 91
22 31 16 99 51 67 63 99 41 92 36 54 22 98 40 99 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 98 36 84 99 99 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 99 99 16 07 97 57 32 16 99 26 79 33 27 98 66
88 36 68 87 99 62 20 72 03 46 33 67 99 55 12 32 63 93 53 69
04 42 16 99 38 25 39 11 24 94 72 99 08 46 29 32 40 62 76 36
20 69 94 00 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''

def diagLRMax(grid, result):
  row_count = len(grid)
  col_count = len(grid[0])
  # r = 3
  # while r < row_count:
  #   c = 0
  #   while r - c > 2:
  #     n0 = grid[r-c][c]
  #     n1 = grid[r-c-1][c+1]
  #     n2 = grid[r-c-2][c+2]
  #     n3 = grid[r-c-3][c+3]
  #     print(f"r: {r-c}, c: {c} n0: {n0} n1: {n1} n2: {n2} n3: {n3}")
  #     if n3 == 0:
  #       c += 3
  #     elif c == 0 or n3 > grid[r-c+1][c-1]:
  #       prod = n0 * n1 * n2 * n3
  #       if prod > result["max"]:
  #         results(result, prod, r, c, "diagLR", (n0, n1, n2, n3))
  #     c += 1
  #
  #   r += 1

  c = 1
  while c < col_count:
    r = row_count - 1
    while r - c > 2:
      n0_col = c + row_count - 1 - r
      n0 = grid[r][n0_col]
      n1 = grid[r-1][n0_col + 1]
      n2 = grid[r-2][n0_col + 2]
      n3 = grid[r-3][n0_col + 3]
      print(f"r: {r}, c: {n0_col} n0: {n0} n1: {n1} n2: {n2} n3: {n3}")
      if n0 == 0:
        r -= 3
      elif r == row_count - 1 or grid[r+1][c + row_count - r] < n3:
        prod = n0 * n1 * n2 * n3
        # print(f"r: {r-c}, c: {c} prod: {prod}")
        if prod > result["max"]:
          results(result, prod, r, c, "diagLR", (n0, n1, n2, n3))
      r -= 1
    print("--------------")
    c += 1
  return result


def to_grid(grid_str):
  lines = grid_str.strip().split('\n')
  for i in range(0, len(lines)):
    lines[i] = list(map(lambda num_str: int(num_str), lines[i].split(' ')))
  return lines

def results(result, max, r, c, dir, nums):
  result["max"] = max
  result["r"] = r
  result["c"] = c
  result["dir"] = dir
  result["nums"] = nums

def max_prod(grid, result):
  row_count = len(grid)
  col_count = len(grid[0])
  max = 0

  for r in range(0, row_count):
    line = grid[r]
    c = 0
    while c < col_count - 3:
      if line[c+3] == 0:
        c += 3
      elif c == 0 or line[c+3] > line[c-1]:
        prod = line[c] * line[c+1] * line[c+2] * line[c+3]
        if prod > result["max"]:
          results(result, prod, r, c, "horiz", (line[c], line[c+1], line[c+2], line[c+3]))
          print(f"max: {result['max']}")
      c += 1

  c = 0
  while c < col_count:
    r = 0
    while r < row_count - 3:
      if grid[r+3][c] == 0:
        r += 3
      elif r == 0 or grid[r+3][c] > grid[r-1][c]:
        prod = grid[r][c] * grid[r+1][c] * grid[r+2][c] * grid[r+3][c]
        if prod > result["max"]:
          results(result, prod, r, c, "vert", (grid[r][c], grid[r+1][c], grid[r+2][c], grid[r+3][c]))
          print(f"max: {result['max']}")
      r += 1
    c += 1

  return result

grid = to_grid(grid_str)
result = {"max": 0, "r": 0, "c": 0, "dir": None, "nums": None}
result = max_prod(grid, result)
result = diagLRMax(grid, result)
result = diagRLMax(grid, result)  #todo
print(result)
expected = 99 ** 4

print(f"exp: {expected}")
assert result["max"] == expected