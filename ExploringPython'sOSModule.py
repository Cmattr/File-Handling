import os

def list_directory_contents(path):
  try:
    for root, dirs, files in os.walk(path):
        for name in files:
            print(os.path.join(root, name))
  except FileNotFoundError:
     print("an error has occured, Please check the file path and try again")
# Prompt the user for the user_directory path
user_directory = input("Enter the user_directory path: ")

def report_file_sizes(user_directory):
    try:
        # Get a list of all files in the specified user_directory
        files = os.listdir(user_directory)
        
        # Iterate through each file and print its name and size
        for filename in files:
            filepath = os.path.join(user_directory, filename)
            if os.path.isfile(filepath):
                size_bytes = os.path.getsize(filepath)
                size_kb = size_bytes / 1024
                print(f"File: {filename} | Size: {size_kb:.2f} KB")
    except FileNotFoundError:
        print(f"Directory '{user_directory}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def count_file_extensions(user_directory):
    extension_counts = {}
    for root, _, files in os.walk(user_directory):
            for file in files:
                _, extension = os.path.splitext(file) 
                extension = extension.lower()  
                if extension:
                    extension_counts[extension] = extension_counts.get(extension, 0) + 1
            for ext, count in extension_counts.items():
                print(f"{ext.upper()[1:]}: {count}")

if __name__ == "__main__":
    target_directory = "/path/to/your/user_directory"
    count_file_extensions(target_directory)

list_directory_contents(user_directory)
report_file_sizes(user_directory)
count_file_extensions(user_directory)