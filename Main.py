import os

def list_directory_contents(path):
    try:
        # Check if the path is a directory
        if not os.path.isdir(path):
            raise NotADirectoryError(f"The path '{path}' is not a directory.")
        
        print(f"Contents of the directory '{path}':")
        
        # List all files and subdirectories
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(f"Directory: {entry.name}")
                elif entry.is_file():
                    print(f"File: {entry.name}")
                else:
                    print(f"Other: {entry.name}")
                    
    except NotADirectoryError as e:
        print(e)
    except PermissionError:
        print(f"Permission denied: Cannot access the directory '{path}'.")
    except FileNotFoundError:
        print(f"File not found: The path '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Prompt the user for the directory path
    path = input("Please enter the directory path: ")
    
    # List the contents of the directory
    list_directory_contents(path)

if __name__ == "__main__":
    main()
