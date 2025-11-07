import os

def count_lines(filename):
    """READS A FILE AND RETURNS THE TOTAL NUMBER OF LINES"""
    try:
        file_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(file_dir, filename)
        with open(file_path, 'r') as file:
            line_count = 0
            for line in file:
                line_count += 1
            return line_count
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

print(f"TOTAL LINES : {count_lines('sample.txt')}")
