import pandas as pd
import numpy as np
import sys

def calculate_total_distance(file_path):
    data = pd.read_csv(file_path, sep='\s+', header=None).to_numpy()

    left_array = data[:, 0]
    right_array = data[:, 1]

    sorted_left = np.sort(left_array)
    sorted_right = np.sort(right_array)

    total_distance = np.sum(np.abs(sorted_left - sorted_right))

    return total_distance

def main():
    if len(sys.argv) != 2:
        print("Usage: python solve_distance.py <file>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        total_distance = calculate_total_distance(file_path)
        print(f"The total distance is: {total_distance}")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
