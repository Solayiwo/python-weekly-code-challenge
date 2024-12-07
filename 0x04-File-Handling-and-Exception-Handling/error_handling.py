#!/usr/bin/python3

file_name = input("Enter your file name: ")

try:
    with open(file_name, "r") as file:
        content = file.read()

    print("File content successfully read:")
    print(content)
except FileNotFoundError:
    error_message = f"Error: The file {file_name} does not exist"
    print(error_message)
except PermissionError:
        error_message = "Error: Permission denied to read/write the file."
        print(error_message)
except Exception as e:
        print(f"An unexpected error occurred: {e}")