import numpy as np
with open('input.txt', "r+") as f:
    input_file = np.array([int(i) for i in f.read().splitlines()])
increasing = 0
for i, _ in enumerate(input_file):
    increasing += 1 if (i > 0 and input_file[i] > input_file[i-1]) else 0
print(increasing)
increasing = 0
for i, _ in enumerate(input_file):
    increasing += 1 if i > 3 and input_file[[i, i-1, i-2]].sum() > input_file[[i-1, i-2, i-3] ].sum() else 0
print(increasing)
