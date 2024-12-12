entries = {}

with open("./input.txt") as file_in:
    for line in file_in:
        given_total, nums_in = line.split(": ")
        entries[int(given_total)] = [int(_) for _ in nums_in.split(" ")]

def check_add(total_in: int, running_total: int, nums_in: list[int]):
    if len(nums_in) == 0:
        return total_in == running_total
    if running_total + nums_in[0] > total_in:
        return False
    else:
        return check_add(total_in, running_total + nums_in[0], nums_in[1:]) or check_mult(total_in, running_total + nums_in[0], nums_in[1:])
    
def check_mult(total_in: int, running_total: int, nums_in: list[int]):
    if len(nums_in) == 0:
        return total_in == running_total
    if running_total * nums_in[0] > total_in:
        return False
    else:
        return check_add(total_in, running_total * nums_in[0], nums_in[1:]) or check_mult(total_in, running_total * nums_in[0], nums_in[1:])

def check_entry(total_in: int, nums_in: list[int]):
    print(f"Checking {total_in} against {nums_in}")
    print(result := check_add(total_in, nums_in[0], nums_in[1:]) or check_mult(total_in, nums_in[0], nums_in[1:]))
    return result

def part_1():
    return sum(k for k, v in entries.items() if check_entry(k, v))

def part_2():
    ...

if __name__ == "__main__":
    print(part_1())
    print(part_2())
