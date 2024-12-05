use std::fs;

fn main() {
    let mut grid: Vec<Vec<&str>> = Vec::new();

    let binding = fs::read_to_string("./input.txt").unwrap();
    for line in binding.lines() {
        grid.push(line.split("").collect());
    }

    println!("Part 1: {}", part_1(grid.clone()));
    println!("Part 2: {}", part_2(grid.clone()));
}

fn part_1(grid_in: Vec<Vec<&str>>) -> i32 {
    let xmas_pattern = ["X", "M", "A", "S"];
    let mut count = 0;

    for (i, row) in grid_in.clone().into_iter().enumerate() {
        for (j, char) in row.clone().into_iter().enumerate() {
            if char == "X" {
                if i >= 3 {
                    count += ([grid_in[i][j], grid_in[i-1][j], grid_in[i-2][j], grid_in[i-3][j]] == xmas_pattern) as i32;
                    if j >= 3 {
                        count += ([grid_in[i][j], grid_in[i-1][j-1], grid_in[i-2][j-2], grid_in[i-3][j-3]] == xmas_pattern) as i32;
                    }
                    if j < row.len() - 3 {
                        count += ([grid_in[i][j], grid_in[i-1][j+1], grid_in[i-2][j+2], grid_in[i-3][j+3]] == xmas_pattern) as i32;
                    }
                }
                if j >= 3 {
                    count += ([grid_in[i][j], grid_in[i][j-1], grid_in[i][j-2], grid_in[i][j-3]] == xmas_pattern) as i32;
                }
                if j < row.len() - 3 {
                    count += ([grid_in[i][j], grid_in[i][j+1], grid_in[i][j+2], grid_in[i][j+3]] == xmas_pattern) as i32;
                }
                if i < grid_in.len() - 3 {
                    count += ([grid_in[i][j], grid_in[i+1][j], grid_in[i+2][j], grid_in[i+3][j]] == xmas_pattern) as i32;
                    if j >= 3 {
                        count += ([grid_in[i][j], grid_in[i+1][j-1], grid_in[i+2][j-2], grid_in[i+3][j-3]] == xmas_pattern) as i32;
                    }
                    if j < row.len() - 3 {
                        count += ([grid_in[i][j], grid_in[i+1][j+1], grid_in[i+2][j+2], grid_in[i+3][j+3]] == xmas_pattern) as i32;
                    }
                }

            }
        }
    }

    return count;
}

fn part_2(grid_in: Vec<Vec<&str>>) -> i32 {
    let mut count = 0;
    let xmas_pattern_1 = [["M", "M"], ["S", "S"]];
    let xmas_pattern_2 = [["M", "S"], ["M", "S"]];
    let xmas_pattern_3 = [["S", "M"], ["S", "M"]];

    for (i, row) in grid_in.clone().into_iter().enumerate() {
        for (j, char) in row.clone().into_iter().enumerate() {
            if char == "A" && i >= 1 && i < grid_in.len() - 1 && j >= 1 && j < row.len() - 1 {
                let found_chars = [[grid_in[i-1][j-1], grid_in[i-1][j+1]], [grid_in[i+1][j-1], grid_in[i+1][j+1]]];
                count += (found_chars == xmas_pattern_1 || found_chars.into_iter().rev().eq(xmas_pattern_1.into_iter()) || found_chars == xmas_pattern_2 || found_chars == xmas_pattern_3) as i32;
            }
        }
    }

    return count;
}
