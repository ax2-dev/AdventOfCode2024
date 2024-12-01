import pandas as pd
import sys
from collections import Counter

def calculate_similarity_score(file_path):
    data = pd.read_csv(file_path, sep='\s+', header=None).to_numpy()

    left_array = data[:, 0]
    right_array = data[:, 1]

    right_counts = Counter(right_array)

    similarity_score = sum(x * right_counts[x] for x in left_array)

    return similarity_score

def main():
    if len(sys.argv) != 2:
        print("Usage: python solve_similarity.py <file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        similarity_score = calculate_similarity_score(file_path)
        print(f"The similarity score is: {similarity_score}")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
