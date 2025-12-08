from readfile import read_file

lines = read_file("inputs/day1/input.txt")

def part1():

  current_value = 50
  zero_count = 0

  for line in lines:
    direction = line[0]
    rotation = int(line[1:])
    
    if rotation >= 100:
      rotation = rotation - (rotation // 100) * 100
    
    if direction == 'L':
      current_value = current_value - rotation
    else:
      current_value = current_value + rotation
    
    if current_value >= 100:
      current_value = current_value - 100
    
    if current_value < 0:
      current_value = current_value + 100
    
    if current_value == 0:
      zero_count = zero_count + 1
  
  return zero_count

def part2():

  current_value = 50
  zero_clicks = 0

  for line in lines:
    direction = line[0]
    rotation = int(line[1:])

    if rotation >= 100:
      zero_clicks = zero_clicks + (rotation // 100)
      rotation = rotation - (rotation // 100) * 100
    
    if direction == 'L':
      new_value = current_value - rotation
      new_value = new_value + 100 if new_value < 0 else new_value
      if (new_value == 0 or new_value > current_value) and current_value != 0:
        zero_clicks = zero_clicks + 1
      current_value = new_value
    else:
      new_value = current_value + rotation
      new_value = new_value - 100 if new_value >= 100 else new_value
      if new_value == 0 or new_value < current_value:
        zero_clicks = zero_clicks + 1
      current_value = new_value

  return zero_clicks

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")

