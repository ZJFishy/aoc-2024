use std::fs;
use regex::Regex;

fn main() {
    let binding = fs::read_to_string("./input.txt").unwrap();
    let line = binding.as_str();

    println!("Part 1: {}", part_1(line));
    println!("Part 2: {}", part_2(line));
}

fn part_1(raw_string: &str) -> i32 {
    let mul_regex = Regex::new(r"mul\((?<a>\d+),(?<b>\d+)\)").unwrap();
    return mul_regex.captures_iter(raw_string)
        .map(|c| c.extract())
        .map(|(_, [a, b])| a.parse::<i32>().unwrap() * b.parse::<i32>().unwrap())
        .sum();
}

fn part_2(raw_string: &str) -> i32 {
    let mul_do_dont_regex = Regex::new(r"mul\(\d+,\d+\)|do\(\)|don't\(\)").unwrap();
    let mut include = true;
    let mut strings_to_include: Vec<&str> = Vec::new();
    let mul_do_dont_strings: Vec<&str> = mul_do_dont_regex.find_iter(raw_string)
        .map(|m| m.as_str())
        .collect();
    for entry in mul_do_dont_strings {
        if entry == "do()" {
            include = true;
        } else if entry == "don't()" {
            include = false;
        } else if include {
            strings_to_include.push(entry);
        }
    }
    let mul_num_regex = Regex::new(r"\((?<a>\d+),(?<b>\d+)\)").unwrap();
    return strings_to_include.into_iter()
        .map(|x| mul_num_regex.captures(x).unwrap().extract())
        .map(|(_, [a, b])| a.parse::<i32>().unwrap() * b.parse::<i32>().unwrap())
        .sum();
}