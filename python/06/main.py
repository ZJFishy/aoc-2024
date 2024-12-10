map_in: list[list[str]] = []

with open("input.txt") as file_in:
    for line in file_in:
        map_in.append([_ for _ in line if _ != "\n"])

def take_map_step(map_in: list[list[str]], guard_location: tuple[int, int]) -> tuple[int, int]:
    guard_row, guard_col = guard_location
    
    if map_in[guard_row][guard_col] == "^":
        try:
            char_above = map_in[guard_row - 1][guard_col]
            if char_above == ".":
                map_in[guard_row - 1][guard_col] = "^"
                map_in[guard_row][guard_col] = "."
                return (guard_row - 1, guard_col)
            else:
                map_in[guard_row][guard_col] = ">"
                return guard_location
        except Exception:
            return (-1, -1)
    elif map_in[guard_row][guard_col] == ">":
        try:
            char_right = map_in[guard_row][guard_col + 1]
            if char_right == ".":
                map_in[guard_row][guard_col + 1] = ">"
                map_in[guard_row][guard_col] = "."
                return (guard_row, guard_col + 1)
            else:
                map_in[guard_row][guard_col] = "v"
                return guard_location
        except Exception:
            return (-1, -1)
    elif map_in[guard_row][guard_col] == "v":
        try:
            char_below = map_in[guard_row + 1][guard_col]
            if char_below == ".":
                map_in[guard_row + 1][guard_col] = "v"
                map_in[guard_row][guard_col] = "."
                return (guard_row + 1, guard_col)
            else:
                map_in[guard_row][guard_col] = "<"
                return guard_location
        except Exception:
            return (-1, -1)
    else:
        try:
            char_left = map_in[guard_row][guard_col - 1]
            if char_left == ".":
                map_in[guard_row][guard_col - 1] = "<"
                map_in[guard_row][guard_col] = "."
                return (guard_row, guard_col - 1)
            else:
                map_in[guard_row][guard_col] = "^"
                return guard_location
        except Exception:
            return (-1, -1)

def find_start(map_passed: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(map_passed):
        for j, char in enumerate(row):
            if char == "^":
                return (i, j)

def part_1(starting_point_passed):
    finished = False
    last_location = starting_point_passed
    visited_locations = [last_location]
    starting_map = [_.copy() for _ in map_in]
    while not finished:
        last_location = take_map_step(starting_map, last_location)
        if last_location == (-1, -1):
            finished = True
        else:
            visited_locations.append(last_location)
    return len(set(visited_locations))

def check_for_loop(map_passed: list[list[str]], starting_location: tuple[int, int]) -> bool:
    visited_positions = [(starting_location, map_passed[starting_location[0]][starting_location[1]])]
    while True:
        starting_location = take_map_step(map_passed, starting_location)
        if starting_location == (-1, -1):
            return False
        position = (starting_location, map_passed[starting_location[0]][starting_location[1]])
        if position in visited_positions:
            return True
        visited_positions.append(position)
    
def part_2(starting_point_passed):
    count = 0
    for i, row in enumerate(map_in):
        for j, char in enumerate(row):
            if char == ".":
                new_map = [_.copy() for _ in map_in]
                new_map[i][j] = "#"
                starting_location = starting_point_passed
                if check_for_loop(new_map, starting_location):
                    count += 1
                
    return count
    
if __name__ == "__main__":
    starting_point = find_start(map_in)
    print(part_1(starting_point))
    print(part_2(starting_point))