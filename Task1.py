#task1 - file to list converter


filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

        stripped_lines = []

        for line in lines:
            stripped_lines.append(line.strip())

        print(stripped_lines)

except FileNotFoundError:
    print("File not found.") 