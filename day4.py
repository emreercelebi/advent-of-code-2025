from readfile import read_file

lines = read_file("inputs/day4/input.txt")
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def part1():
  count = 0
  for row in range(len(lines)):
    for col in range(len(lines[row])):
      if lines[row][col] == '@':
        surrounding = 0
        for dir in dirs:
          temp_row = row + dir[0]
          temp_col = col + dir[1]
          if temp_row < 0 or temp_row >= len(lines) or temp_col < 0 or temp_col >= len(lines[row]):
            continue
          if lines[temp_row][temp_col] == '@':
            surrounding += 1
        if surrounding < 4:
          count += 1

  return count

def part2():
  grid = [list(line) for line in lines]
  count = 0
  rolls_removed = -1

  while rolls_removed != 0:
    rolls_removed = 0
    cells_to_update = []
    for row in range(len(grid)):
      for col in range(len(grid[row])):
        if grid[row][col] == '@':
          surrounding = 0
          for dir in dirs:
            temp_row = row + dir[0]
            temp_col = col + dir[1]
            if temp_row < 0 or temp_row >= len(grid) or temp_col < 0 or temp_col >= len(grid[row]):
              continue
            if grid[temp_row][temp_col] == '@':
              surrounding += 1
          if surrounding < 4:
            cells_to_update.append((row, col))
    
    rolls_removed = len(cells_to_update)
    count += rolls_removed
    for cell in cells_to_update:
      grid[cell[0]][cell[1]] = '.'


  return count


print(f"Part 1: {part1()}") 
print(f"Part 2: {part2()}")