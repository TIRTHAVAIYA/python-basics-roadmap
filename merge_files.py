import os

def merge_files(file1, file2, merged_file):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file1_path = os.path.join(script_dir, file1)
        file2_path = os.path.join(script_dir, file2)
        merged_path = os.path.join(script_dir, merged_file)

        # Read contents of both files
        with open(file1_path, 'r') as f1:
            content1 = f1.read()

        with open(file2_path, 'r') as f2:
            content2 = f2.read()

        # Merge them (add a separator line for clarity)
        merged_content = content1 + "\n\n--- MERGED CONTENT ---\n\n" + content2

        # Write to the merged file
        with open(merged_path, 'w') as mf:
            mf.write(merged_content)

        return f"Files '{file1}' and '{file2}' successfully merged into '{merged_file}'."

    except FileNotFoundError as e:
        return f"Error: {e.filename} not found."
    except PermissionError:
        return f"Error: Permission denied while writing '{merged_file}'."

# Example usage
print(merge_files('sample1.txt', 'sample2.txt', 'merged_output.txt'))
