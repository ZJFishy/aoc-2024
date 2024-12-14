antenna_map: list[list[str]] = []

with open("./input.txt") as file_in:
    antenna_map = [[*line] for line in file_in]

height, width = len(antenna_map), len(antenna_map[0])

def find_all_antennae(antenna_char: str) -> list[tuple[int, int]]:
    """
    Returns the coordinates of all antennae of a given type
    """
    antennae = []

    for i, row in enumerate(antenna_map):
        for j, char in enumerate(row):
            if char == antenna_char:
                antennae.append((i, j))

    return antennae

def find_antinodes(antennae_coords: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Returns the coordinates of all antenna antinodes given antennae coordinates
    """
    antinodes = []
    for coord_1 in antennae_coords:
        for coord_2 in antennae_coords:
            if coord_1 != coord_2:
                x_diff, y_diff = [y - x for x, y in zip(coord_1, coord_2)]

                if ((0 <= (new_x := coord_1[0] - x_diff) < height) and
                    (0 <= (new_y := coord_1[1] - y_diff) < width)):
                    antinodes.append((new_x, new_y))
                if ((0 <= (new_x := coord_2[0] + x_diff) < height) and
                    (0 <= (new_y := coord_2[1] + y_diff) < width)):
                    antinodes.append((new_x, new_y))

    return antinodes

def part_1():
    """
    Count the unique antinodes in the map
    """
    checked_antennae = []
    antinode_coords = []

    for row in antenna_map:
        for char in row:
            if char not in [".", "\n"] and char not in checked_antennae:
                print(char)
                checked_antennae.append(char)
                antennae = find_all_antennae(char)
                print(antennae)
                antinodes = find_antinodes(antennae)
                print(antinodes)
                for a in antinodes:
                    if a not in antinode_coords:
                        antinode_coords.append(a)

    return len(antinode_coords)

def part_2():
    ...
    
if __name__ == "__main__":
    print(part_1())
    print(part_2())
