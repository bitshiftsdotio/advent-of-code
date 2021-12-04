import collections

f = open('input.txt', 'r')

values = f.readlines()

gamma_rate = ''
epsilon_rate = ''

# Get the number of bits in each value. This code assumes that all values have the same number of bits,
# which they certainly appear to.
value_length = len(values[0])

# For each bit position in each value...
for i in range(0, 12):
    # Get all the bits in that position, using a list comprehension.
    bits = [s[i] for s in values]

    # Figure out which bit is the most common.
    # We can use collections.Counter for this.
    counter = collections.Counter(bits)
    most_common_bit = max(bits, key=counter.get)
    least_common_bit = min(bits, key=counter.get)

    # Add the most and least common bits to the gamma and epsilon rate values respectively.
    gamma_rate += most_common_bit
    epsilon_rate += least_common_bit

# Convert each value from its binary representation into an integer.
gamma_rate_integer = int(gamma_rate, 2)
epsilon_rate_integer = int(epsilon_rate, 2)

print(gamma_rate_integer * epsilon_rate_integer)