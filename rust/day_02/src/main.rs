use std::{fs, iter::zip};

fn main() {
    let mut results: Vec<Vec<i32>> = Vec::new();

    for line in fs::read_to_string("./input.txt").unwrap().lines() {
        let split_line = line.split_whitespace();
        let mut report: Vec<i32> = Vec::new();
        split_line.for_each(|x| report.push(x.parse().unwrap()));
        results.push(report);
    }

    let mut report_diffs: Vec<Vec<i32>> = Vec::new();
    results.into_iter().for_each(|x| report_diffs.push(find_report_differences(x)));
    
    let mut good_report_diffs: Vec<Vec<i32>> = Vec::new();
    let mut bad_report_diffs: Vec<Vec<i32>> = Vec::new();

    report_diffs.iter().for_each(|x| match check_report_exact(x.clone()) {
        true => {good_report_diffs.push(x.clone());},
        false => {bad_report_diffs.push(x.clone());},
    });

    println!("Part 1: {}", good_report_diffs.len());

    let mut new_safes = 0;
    bad_report_diffs.iter().for_each(|x| match check_report_tolerate(x.clone()) {
        true => {new_safes += 1;},
        false => {},
    });
    println!("Part 2: {}", good_report_diffs.len() + new_safes);
}

fn find_report_differences(report: Vec<i32>) -> Vec<i32> {
    let mut report_diffs: Vec<i32> = Vec::new();
    zip(&report[..(report.len()-1)], &report[1..]).for_each(|(i, j)| report_diffs.push(i - j));
    return report_diffs;
}

fn check_report_exact(report_diff: Vec<i32>) -> bool {
    return report_diff.iter().all(|x| 1 <= *x && *x <= 3) || report_diff.iter().all(|x| -1 >= *x && *x >= -3);
}

fn check_report_tolerate(report_diff: Vec<i32>) -> bool {
    for i in 0..(report_diff.len()-1) {
        let mut diff_copy = report_diff.clone();
        let diff_sum = diff_copy[i] + diff_copy[i+1];
        diff_copy[i] = diff_sum;
        diff_copy.remove(i+1);
        if check_report_exact(diff_copy) {
            return true;
        }
    }
    return check_report_exact(report_diff[1..].to_vec()) || check_report_exact(report_diff[..(report_diff.len()-1)].to_vec());
}