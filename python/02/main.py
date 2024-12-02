import numpy as np

reports = []

with open("./input.txt") as file_in:
    for line in file_in:
        levels = [int(_) for _ in line.split()]
        reports.append(levels)
        
def find_report_differences(report: list[int]):
    return np.array(report[:-1]) - np.array(report[1:])

report_differences = [find_report_differences(_) for _ in reports]

def check_report_exact(report_diff: np.ndarray) -> bool:
    return (sum((np.full_like(report_diff, 1) <= report_diff) & (report_diff <= np.full_like(report_diff, 3))) == len(report_diff)
        or sum((np.full_like(report_diff, -1) >= report_diff) & (report_diff >= np.full_like(report_diff, -3))) == len(report_diff))
    

good_report_differences = []
bad_report_differences = []
for report_diff in report_differences:
    if check_report_exact(report_diff):
        good_report_differences.append(report_diff)
    else:
        bad_report_differences.append(report_diff)

def part_1() -> int:
    return len(good_report_differences)

def check_report_tolerate(report_diff: np.ndarray) -> bool:
    for i in range(len(report_diff) - 1):
        diff_copy = report_diff.copy()
        diff_sum = diff_copy[i] + diff_copy[i+1]
        diff_copy[i] = diff_sum
        diff_copy = np.delete(diff_copy, i+1)
        if check_report_exact(diff_copy):
            return True
    return check_report_exact(report_diff[1:]) or check_report_exact(report_diff[:-1])
    
def part_2() -> int:
    return sum(check_report_tolerate(_) for _ in bad_report_differences)

if __name__ == "__main__":
    print(p1_result := part_1())
    print(p1_result + part_2())