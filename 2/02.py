from collections import defaultdict
directions = defaultdict(lambda: 0)
with open('input.txt', "r+") as f:
    input_file = f.read().splitlines()
for line in input_file :
    key, val = line.split()
    directions[key] += int(val)
result = directions['forward'] * (directions['down'] - directions['up'])
print(result)
#Part2
position = directions['forward'] 
depth = 0
aim = 0
for line in input_file :
    key, val = line.split()
    if key == 'forward':
        depth += aim * int(val)
    elif key == 'up':
        aim -= int(val)
    elif key == 'down':
        aim += int(val)
result = position * depth
print(result)