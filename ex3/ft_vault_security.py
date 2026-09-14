def secure_archive(file_name: str, mode: str = "r", w_content: str = ""
                   ) -> tuple[bool, str]:
    try:
        with open(file_name, mode) as file:
            if mode == "r":
                content = file.read()
            elif mode == "w":
                file.write(w_content)
    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))
    if mode == "w":
        return (True, "Content successfully written to file")
    return (True, content)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("Inaccesible.txt"))
    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("texto_ejemplo.txt"))
    data = secure_archive("texto_ejemplo.txt")
    print("\nUsing 'secure_archive' to read from a noexistent file:")
    print(secure_archive("new_file.txt", "w", data[1]))
