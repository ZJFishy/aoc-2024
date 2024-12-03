import re

with open("./input.txt") as file_in:
    raw_string = file_in.read()

mul_strings = re.findall(r"(mul\(\d+,\d+\))", raw_string)
parsed_strings = [m[4:-1].split(",") for m in mul_strings]

def part_1():
    return sum(int(p[0]) * int(p[1]) for p in parsed_strings)

def part_2():
    ...

if __name__ == "__main__":
    print(part_1())
    print(part_2())