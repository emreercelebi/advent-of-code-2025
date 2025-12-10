from readfile import read_file

lines = read_file("inputs/day6/input.txt")

def part1():
  rows = [line.split() for line in lines]
  total = 0
  for col in range(len(rows[0])):
    operation = rows[len(rows) - 1][col]
    subtotal = 0 if operation == '+' else 1
    for row in range(len(rows) - 1):
      val = int(rows[row][col])
      if operation == '+':
        subtotal += val
      else:
        subtotal *= val
    total += subtotal
  
  return total

def part2():
  operation_idxs = []
  operation_line = lines[len(lines) - 1]
  for i in range(len(operation_line)):
    if operation_line[i] != " ":
      operation_idxs.append(i)
  operation_idxs.append(len(operation_line) + 1)

  total = 0
  for op_idx in range(len(operation_idxs) - 1):
    operation = lines[len(lines) - 1][operation_idxs[op_idx]]
    subtotal = 0 if operation == '+' else 1
    
    for col in range(operation_idxs[op_idx], operation_idxs[op_idx + 1] - 1):
      val = 0
      multiplier = 1
      for row in range(len(lines) - 2, -1, -1):
        if lines[row][col] != " ":
          val += int(lines[row][col]) * multiplier
          multiplier *= 10
      if operation == '+':
        subtotal += val
      else:
        subtotal *= val
    total += subtotal
  
  return total

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")