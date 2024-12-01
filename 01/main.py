left = []
right = []

with open("./input.txt") as file_in:
    for line in file_in:
        split_line = line.split()
        left.append(int(split_line[0]))
        right.append(int(split_line[1]))

left.sort()
right.sort()
        
def part_1():    

    sum_of_diffs = 0

    for left_num, right_num in zip(left, right):
        sum_of_diffs += abs(left_num - right_num)
        
    return sum_of_diffs

def part_2():
    right_counts = {}
    
    for entry in right:
        if right_counts.get(entry):
            right_counts[entry] += 1
        else:
            right_counts[entry] = 1
    
    sum_of_similarity = 0
    
    for entry in left:
        if entry_count := right_counts.get(entry):
            sum_of_similarity += entry_count * entry
    
    return sum_of_similarity

if __name__ == "__main__":
    print(part_1())
    print(part_2())