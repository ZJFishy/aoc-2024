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
    # return check_add(total_in, nums_in[0], nums_in[1:]) or check_mult(total_in, nums_in[0], nums_in[1:])
    if len(nums_in) == 1:
        return total_in == nums_in[0]
    good = False
    current_num = nums_in.pop()
    # print(f"{total_in:<12}\t{current_num:<12}\t{nums_in}")
    if total_in % current_num == 0:
        good = good or check_entry(total_in // current_num, nums_in.copy())
    if total_in > current_num:
        good = good or check_entry(total_in - current_num, nums_in.copy())
    else:
        return False
    return good

def part_1():
    good_totals = [k for k, v in {k: v for k, v in entries.items()}.items() if check_entry(k, v)]
    for k, v in entries.items():
        if k not in good_totals:
            print(k, v)
    print(sum(k for k in entries.keys()))
    return sum(good_totals)

def part_2():
    ...

if __name__ == "__main__":
    print(part_1())
    print(part_2())
