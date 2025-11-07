import os

def copy_file(sample_file, destination_file):
    try:
        
        file_dir = os.path.dirname(os.path.abspath(__file__))
        sample_path = os.path.join(file_dir, sample_file)
        destination_path = os.path.join(file_dir, destination_file)

        with open(sample_path, 'r') as sample:
            content = sample.read()

        with open(destination_path, 'w') as destination:
            destination.write(content)

        return f"✅ Content copied successfully from '{sample_file}' to '{destination_file}'."

    except FileNotFoundError:
        return f"Error: The file '{sample_file}' was not found."
    except PermissionError:
        return f"Error: Permission denied for '{destination_file}'."

print(copy_file('sample.txt', 'destination.txt'))
