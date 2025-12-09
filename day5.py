from readfile import read_file
from typing import List, Tuple, Optional

lines = read_file("inputs/day5/input.txt")

def extract_lists() -> Tuple[List[Tuple[int]], List[int]]:
  """
  Parses input file to extract intervals as a lis tof tuples and
  the ids as a list of ints

  :returns: two lists, one with interval tuples, and another with ids to check
  """

  intervals = []
  ids = []

  for line in lines:
    if '-' in line:
      split_interval = line.split('-')
      intervals.append((int(split_interval[0]), int(split_interval[1])))
    elif len(line) > 0:
      ids.append(int(line))

  return intervals, ids

def build_merged_intervals(intervals: List[Tuple[int]]) -> List[List[int]]:
  intervals = sorted(intervals)
  merged_intervals_result = [[intervals[0][0], intervals[0][1]]]

  current_interval = merged_intervals_result[0]
  for i in range(1, len(intervals)):
    if intervals[i][0] <= current_interval[1]:
      current_interval[1] = max(current_interval[1], intervals[i][1])
    else:
      current_interval = [intervals[i][0], intervals[i][1]]
      merged_intervals_result.append(current_interval)
  
  return merged_intervals_result

def binary_search_interval(intervals: List[List[int]], target) -> Optional[List[int]]:
  """
  Uses binary search to look for the interval with the largest
  start value less than or equal to target
  
  :param intervals: List of intervals (2-length arrays)
  :type intervals: List[List[int]]
  :param target: value to compare against interval start values
  :returns: interval with largest start value <= target, or None if no such value exists
  """
  if len(intervals) == 0:
    return None
  
  low = 0
  high = len(intervals) - 1
  result = None

  while low <= high:
    mid = (low + high) // 2
    val = intervals[mid][0]

    if val == target:
      return val
    elif val > target:
      high = mid - 1
    elif val < target:
      low = mid + 1
      result = intervals[mid]
  
  return result

def part1():
  intervals, ids = extract_lists()
  merged_intervals = build_merged_intervals(intervals)

  count = 0
  for item_id in ids:
    matching_interval = binary_search_interval(merged_intervals, item_id)
    if matching_interval is None:
      continue
    if matching_interval[1] >= item_id:
      count += 1

  return count

def part2():
  intervals, _ = extract_lists()
  merged_intervals = build_merged_intervals(intervals)

  total = 0
  for interval in merged_intervals:
    total += interval[1] - interval[0] + 1

  return total

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
