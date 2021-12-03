with open('input.txt', "r+") as f:
    input_file = f.read().splitlines()

#part1
gamma = ""
epsilon  = ""
for i in range(len(input_file[0])):
    all_bits = [x[i] for x in input_file]
    gamma += str(max(set(all_bits), key = all_bits.count))
    epsilon += str(min(set(all_bits), key = all_bits.count))
print(int(gamma, 2) * int(epsilon, 2))

#part2
oxygen_dict = [x for x in input_file]
co2_dict = [x for x in input_file]
for i in range(len(input_file[0])):
    all_bits = [int(x[i]) for x in oxygen_dict]
    target = int((max(set(all_bits), key = all_bits.count))) if not all_bits.count(1) == all_bits.count(0) else 1
    oxygen_dict = [x for x in oxygen_dict if int(x[i]) == int(target)]
    if len(oxygen_dict) == 1:
        break
for i in range(len(input_file[0])):
    all_bits = [int(x[i]) for x in co2_dict]
    target = int((min(set(all_bits), key = all_bits.count))) if not all_bits.count(1) == all_bits.count(0) else 0
    co2_dict = [x for x in co2_dict if int(x[i]) == int(target)]
    if len(co2_dict) == 1:
        break
print(int(oxygen_dict[0], 2) * int(co2_dict[0], 2))