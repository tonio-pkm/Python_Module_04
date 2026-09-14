import sys
from typing import TextIO


def read_display(file_stream: TextIO) -> None:
    print("---\n")
    print(file_stream.read())
    print("---")


def write_display(file_stream: TextIO) -> None:
    file_stream.seek(0)
    print("Transform data:")
    print("---\n")
    lines = file_stream.readlines()
    new_lines = "".join(lines)
    display_lines = ""
    for char in new_lines:
        if char == "\n":
            display_lines += "#"
        display_lines += char
    display_lines += "#"
    print(display_lines)
    print("---")
    try:
        new_file = open(input("Enter new file name (or empty): "), "w")
    except FileNotFoundError:
        print("Not saving data.")
        return
    print(f"Saving data to {new_file.name}")
    new_file.write(display_lines)
    print(f"Data saved in {new_file.name}")


def file_reader() -> None:
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>)")
        return
    try:
        print(f"Accesing file '{sys.argv[1]}'")
        with open(sys.argv[1], "r+") as file:
            read_display(file)
    except FileNotFoundError as e:
        print(f"Error opening '{sys.argv[1]}': {e}")
        return
    except PermissionError as e:
        print(f"Error opening the file '{sys.argv[1]}': {e}")
        return
    print(f"File '{sys.argv[1]}' closed.\n")
    with open(sys.argv[1], "r+") as file:
        write_display(file)


if __name__ == "__main__":
    file_reader()
