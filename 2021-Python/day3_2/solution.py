import collections

f = open('input.txt', 'r')

values = [s.rstrip() for s in f.readlines()]

oxygen_generator = 0
co2_scrubber = 0

# Get the number of bits in each value. This code assumes that all values have the same number of bits,
# which they certainly appear to.
value_length = len(values[0])

# Use a list comprehension to get all of the values for each item.
# We want the oxygen generator values to have all of the values which start with the most common bit,
# and vice versa.
initial_bits = [s[0] for s in values]

counter = collections.Counter(initial_bits)
initial_most_common_bit = max(initial_bits, key=counter.get)
initial_least_common_bit = min(initial_bits, key=counter.get)

oxygen_generator_values = [s for s in values if s.startswith(initial_most_common_bit)]
co2_scrubber_values = [s for s in values if s.startswith(initial_least_common_bit)]

# Continuously filter down the lists until we have only one value in each.
# For the oxygen generator values, we want to discard any values which contain the
# least common bit in each given position, and vice versa.
index = 0
while len(oxygen_generator_values) > 1:
    bits = [s[index] for s in oxygen_generator_values]

    counter = collections.Counter(bits)
    most_common_bit = max(bits, key=counter.get)
    least_common_bit = min(bits, key=counter.get)

    # If either of the bits isn't in the list, we should continue as we don't need to do any filtering
    if '0' not in bits or '1' not in bits:
        index += 1
        continue

    # If there's an equal number of each bit in the given position, we should pick all the values with a 1 in that
    # position. We know this is the case if the most common bit and least common bit are the same.
    if most_common_bit == least_common_bit:
        oxygen_generator_values = [v for v in oxygen_generator_values if v[index] == '1']
    else:
        oxygen_generator_values = [v for v in oxygen_generator_values if v[index] == most_common_bit]

    index += 1

index = 0
while len(co2_scrubber_values) > 1:
    bits = [s[index] for s in co2_scrubber_values]

    counter = collections.Counter(bits)
    most_common_bit = max(bits, key=counter.get)
    least_common_bit = min(bits, key=counter.get)

    # If either of the bits isn't in the list, we should continue as we don't need to do any filtering
    if '0' not in bits or '1' not in bits:
        index += 1
        continue

    # If there's an equal number of each bit in the given position, we should pick all the values with a 0 in that
    # position. We know this is the case if the most common bit and least common bit are the same.
    if most_common_bit == least_common_bit:
        co2_scrubber_values = [v for v in co2_scrubber_values if v[index] == '0']
    else:
        co2_scrubber_values = [v for v in co2_scrubber_values if v[index] == least_common_bit]

    index += 1

# By now, there should only be one value in each list.
# Convert that value from its binary representation into an integer.
oxygen_generator = int(oxygen_generator_values[0], 2)
co2_scrubber = int(co2_scrubber_values[0], 2)

print(oxygen_generator, co2_scrubber, oxygen_generator * co2_scrubber)
