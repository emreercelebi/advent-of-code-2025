from readfile import read_file

lines = read_file("inputs/day7/input.txt")

def part1():
  total_splits = 0
  start_idx = lines[0].index("S")
  beam_idxs = set([start_idx])

  for i in range(1, len(lines) - 1):
    row = lines[i]
    prev = list(beam_idxs)
    idxs_to_add = []
    for idx in prev:
      if row[idx] == '^':
        total_splits += 1
        beam_idxs.remove(idx)
        if idx > 0:
          idxs_to_add.append(idx - 1)
        if idx < len(row) - 1:
          idxs_to_add.append(idx + 1)
    
    for idx in idxs_to_add:
      beam_idxs.add(idx)

  return total_splits

def part2():
  start_idx = start_idx = lines[0].index("S")
  grid = [list(line) for line in lines]
  beam_idxs = {start_idx: 1}

  for i in range(1, len(lines) - 1): 
    row = grid[i]
    prev = dict(beam_idxs)
    idxs_to_add = {}
    for idx in prev:
      if row[idx] == '^':
        val = beam_idxs[idx]
        del beam_idxs[idx]
        for new_idx in [idx - 1, idx + 1]:
          if new_idx in idxs_to_add:
            idxs_to_add[new_idx] += val
          else:
            idxs_to_add[new_idx] = val
           
    for idx in idxs_to_add:
      beam_idxs[idx] = idxs_to_add[idx]
      if idx in prev:
        beam_idxs[idx] += prev[idx]
      
  total = 0
  for val in beam_idxs.values():
    total += val

  return total
             
print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
