input_file = open("input.txt", "r")

measurements = [int(m) for m in input_file.readlines()]

previous = None
current = None
num_greater = 0

for idx, val in enumerate(measurements):
    previous = current

    list_slice = measurements[idx:idx + 3]

    if len(list_slice) != 3:
        break

    current = sum(list_slice)

    if previous is None:
        continue

    if current > previous:
        num_greater += 1

print(num_greater)
