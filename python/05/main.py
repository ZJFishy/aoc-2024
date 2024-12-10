ordering_before: dict[int, list[int]] = {}  # lists of numbers that must come before the key
updates: list[list[int]] = []

with open("./input.txt") as file_in:
    for line in file_in:
        if len(order_rule := line.split("|")) == 2:
            if ordering_before.get(int(order_rule[1])) is None:
                ordering_before[int(order_rule[1])] = [int(order_rule[0])]
            else:
                ordering_before[int(order_rule[1])].append(int(order_rule[0]))
        elif len(update := line.split(",")) > 1:
            updates.append([int(_) for _ in update])

print(ordering_before)
print(updates)

bad_updates = []

def check_update(update: list[int]) -> bool:
    for i, entry in enumerate(update):
        good_befores = [x for x in update[:i] if ((ordering_before.get(entry) is None) or (x in ordering_before[entry]))]
        if (i == 0 and ordering_before.get(entry) is not None and [_ for _ in update if _ in ordering_before.get(entry)] != []) or len(good_befores) != len(update[:i]):
            return False
    return True

def part_1():
    good_updates = []
    good_update_middles = []
    
    for u in updates:
        if check_update(u):
            good_updates.append(u)
            good_update_middles.append(u[len(u) // 2])
        else:
            bad_updates.append(u)
            
    return sum(good_update_middles)

def order_nums(nums_in: list[int]) -> list[int]:
    if len(nums_in) == 1:
        return nums_in
    
    for num in nums_in:     # checking if this can come first
        first = True
        for n in nums_in:   # check all other numbers to see if they need to come first out of the two
            if num != n and ordering_before.get(num) is not None and n in ordering_before.get(num):  # if any number n has to come first, num can't be first
                first = False
                break
        if first:
            nums_in.remove(num)
            sol = [num]
            sol.extend(order_nums(nums_in))
            return sol          
    
def part_2():
    new_good_update_middles = []
    
    for u in bad_updates:
        u_new = order_nums(u)
        new_good_update_middles.append(u_new[len(u_new) // 2])
            
    return sum(new_good_update_middles)

if __name__ == "__main__":
    print(part_1())
    print(part_2())