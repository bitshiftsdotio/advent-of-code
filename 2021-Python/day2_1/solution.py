import typing


def create_instruction_data(instruction: str) -> typing.Dict:
    split_result = instruction.split(" ")

    if len(split_result) != 2:
        raise ValueError("Invalid instruction string.")

    try:
        return {
            "direction": split_result[0],
            "units": int(split_result[1])
        }
    except ValueError as e:
        raise ValueError("Invalid instruction string.", e)


f = open("input.txt", "r")

instructions = [create_instruction_data(line) for line in f.readlines()]

horizontal_position = 0
depth = 0

for i in instructions:
    match i["direction"]:
        case 'forward':
            horizontal_position += i["units"]
        case 'up':
            depth -= i["units"]
        case 'down':
            depth += i["units"]
        case _:
            raise RuntimeError(f'Invalid direction {i["direction"]} while parsing instructions.')

print(horizontal_position * depth)