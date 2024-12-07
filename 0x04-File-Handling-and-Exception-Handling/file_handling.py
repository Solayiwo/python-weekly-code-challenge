#!/usr/bin/python3

with open("index.txt", "r") as file:
    data = file.read()

# modified_content = f"{data} \nI love python programming language."
modified_content = input("Enter text to modify index.txt\n")
modified_content = "{}\n{}".format(data, modified_content)

with open("output.txt", "w")  as new_file:
    modified_data = new_file.write(modified_content)

message = "Modified version of index file hase been saved to output file."
print(message)


