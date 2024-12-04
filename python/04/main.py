grid: list[list[str]] = []

with open("./input.txt") as file_in:
    for line in file_in:
        grid.append([_ for _ in line if _ != "\n"])

def part_1():
    xmas_pattern = ["X", "M", "A", "S"]
    count = 0

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "X":
                if i >= 3:
                    # check north
                    count += int([grid[i][j], grid[i-1][j], grid[i-2][j], grid[i-3][j]] == xmas_pattern)
                    if j >= 3:
                        # check northwest
                        count += int([grid[i][j], grid[i-1][j-1], grid[i-2][j-2], grid[i-3][j-3]] == xmas_pattern)
                    if j < len(row) - 3:
                        # check northeast
                        count += int([grid[i][j], grid[i-1][j+1], grid[i-2][j+2], grid[i-3][j+3]] == xmas_pattern)
                if j >= 3:
                    # check west
                    count += int([grid[i][j], grid[i][j-1], grid[i][j-2], grid[i][j-3]] == xmas_pattern)
                if j < len(row) - 3:
                    # check east
                    count += int([grid[i][j], grid[i][j+1], grid[i][j+2], grid[i][j+3]] == xmas_pattern)
                if i < len(grid)-3:
                    # check south
                    count += int([grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]] == xmas_pattern)
                    if j >= 3:
                        # check southwest
                        count += int([grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3]] == xmas_pattern)
                    if j < len(row) - 3:
                        # check southeast
                        count += int([grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]] == xmas_pattern)
                    
    return count

def part_2():
    count = 0

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "A" and i >= 1 and i < len(grid) - 1 and j >= 1 and j < len(row) - 1:
                xmas_pattern_1 = [["M", "M"], ["S", "S"]]
                xmas_pattern_2 = [["M", "S"], ["M", "S"]]
                xmas_pattern_3 = [["S", "M"], ["S", "M"]]
                found_chars = [[grid[i-1][j-1], grid[i-1][j+1]], [grid[i+1][j-1], grid[i+1][j+1]]]
                if (found_chars == xmas_pattern_1
                    or found_chars == xmas_pattern_1[::-1]
                    or found_chars == xmas_pattern_2
                    or found_chars == xmas_pattern_3):
                    count += 1
    
    return count


if __name__ == "__main__":
    print(part_1())
    print(part_2())