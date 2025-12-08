from readfile import read_file

lines = read_file("inputs/day2/input.txt")

intervals = lines[0].split(",")

def part1():
  total = 0
  for interval in intervals:
    values = interval.split("-")
    low = int(values[0])
    high = int(values[1])
    if len(values[0]) == 1:
      first_half = 1
    else:
      first_half = int(values[0][:(len(values[0]) // 2)])

    invalid_id = int(f"{first_half}{first_half}")
    while invalid_id < low:
      first_half += 1
      invalid_id = int(f"{first_half}{first_half}")

    while invalid_id <= high:
      total += invalid_id
      first_half += 1
      invalid_id = int(f"{first_half}{first_half}")
  
  return total

def part2():
  total = 0
  values_added = set()
  for interval in intervals:
    values = interval.split("-")
    low = int(values[0])
    high = int(values[1])

    for reps in range(2, 11):
      repeated_val = 1
      invalid_id = int(str(repeated_val) * reps)
      while invalid_id < low:
        repeated_val += 1
        invalid_id = int(str(repeated_val) * reps)
      while invalid_id <= high:
        if invalid_id not in values_added:
          total += invalid_id
          values_added.add(invalid_id)
        repeated_val += 1
        invalid_id = int(str(repeated_val) * reps)
  
  return total

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
