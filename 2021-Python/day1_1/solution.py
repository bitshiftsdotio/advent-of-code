input_file = open("input.txt", "r")

measurements = [int(m) for m in input_file.readlines()]

num_greater = 0

for idx, val in enumerate(measurements):
    if idx == 0:
        continue

    if val > measurements[idx - 1]:
        num_greater += 1

print(num_greater)