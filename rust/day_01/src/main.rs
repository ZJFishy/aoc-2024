use std::{collections::HashMap, fs, iter::zip};

fn main() {
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();
    for line in fs::read_to_string("./input.txt").unwrap().lines() {
        let mut split_line = line.split_whitespace();
        left.push(split_line.next().expect("whitespace").parse().unwrap());
        right.push(split_line.next().expect("whitespace").parse().unwrap());
    };

    left.sort();
    right.sort();

    let mut sum_of_diffs: i32 = 0;

    for (left_num, right_num) in zip(left.clone(), right.clone()) {
        sum_of_diffs += (left_num - right_num).abs();
    };

    println!("Sum of differences: {}", sum_of_diffs);

    let mut right_counts = HashMap::new();

    for entry in right {
        if right_counts.get(&entry) != None {
            right_counts.insert(entry, right_counts.get(&entry).unwrap() + 1);
        } else {
            right_counts.insert(entry, 1);
        }
    };

    let mut sum_of_similarity = 0;

    for entry in left {
        if right_counts.get(&entry) != None {
            sum_of_similarity += entry * right_counts.get(&entry).unwrap();
        }
    };

    println!("Sum of similarities: {}", sum_of_similarity);
}
