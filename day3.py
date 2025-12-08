from readfile import read_file

lines = read_file("inputs/day3/input.txt")

def part1():
    total = 0

    for line in lines:
        nums = [int(x) for x in line]
        tens_digit = nums[len(nums) - 2]
        tens_digit_idx = len(nums) - 2

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= tens_digit:
                tens_digit = nums[i]
                tens_digit_idx = i
        
        ones_digit = max(nums[tens_digit_idx + 1:])

        joltage = tens_digit * 10 + ones_digit
        total += joltage

    return total

def part2():
    total = 0

    for line in lines:
        nums = [int(x) for x in line]
        idxs = [i for i in range(len(nums) - 12, len(nums))]
        prev_idx = -1
        for i in range(len(idxs)):
            new_idx = idxs[i]
            for j in range(new_idx, prev_idx, -1):
                if nums[j] >= nums[new_idx]:
                    new_idx = j
            idxs[i] = new_idx
            prev_idx = new_idx
        
        joltage = int("".join([line[i] for i in idxs]))
        total += joltage
    
    return total            


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
