import sys
from typing import TextIO


def read_display(file_stream: TextIO) -> None:
    print("---\n")
    print(file_stream.read())
    print("---")


def file_reader() -> None:
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>)")
        return
    try:
        print(f"Accesing file '{sys.argv[1]}'")
        with open(sys.argv[1], "r") as file:
            read_display(file)
    except FileNotFoundError as e:
        print(f"Error opening '{sys.argv[1]}': {e}")
        return
    except PermissionError as e:
        print(f"Error opening the file '{sys.argv[1]}': {e}")
        return
    print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    file_reader()

