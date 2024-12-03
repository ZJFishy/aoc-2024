import re

with open("./input.txt") as file_in:
    raw_string = file_in.read()

def part_1():
    mul_strings = re.findall(r"(mul\(\d+,\d+\))", raw_string)
    parsed_strings = [m[4:-1].split(",") for m in mul_strings]
    return sum(int(p[0]) * int(p[1]) for p in parsed_strings)

def part_2():
    mul_do_dont_strings = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", raw_string)
    include = True
    strings_to_include = []
    for entry in mul_do_dont_strings:
        if include and entry not in ("do()", "don't()"):
            strings_to_include.append(entry)
        elif entry == "don't()":
            include = False
        elif entry == "do()":
            include = True
    parsed_strings = [s[4:-1].split(",") for s in strings_to_include]
    return sum(int(p[0]) * int(p[1]) for p in parsed_strings)

if __name__ == "__main__":
    print(part_1())
    print(part_2())