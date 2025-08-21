def modify_content(content, mode="upper"):
    """
    Modify the content based on the chosen mode.
    - "upper": convert text to uppercase.
    - "number": add line numbers to each line.
    """
    if mode == "upper":
        return content.upper()
    elif mode == "number":
        lines = content.splitlines()
        numbered_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]
        return "\n".join(numbered_lines)
    else:
        return content  # return as-is if unknown mode


def main():
    try:
        # Ask user for input filename
        input_file = input("Enter filename to read: ")

        # Try to open and read the file
        with open(input_file, "r") as file:
            content = file.read()

        # Ask user which modification to apply
        print("Choose modification type:")
        print("1. Convert to UPPERCASE")
        print("2. Add line numbers")
        choice = input("Enter choice (1 or 2): ")

        if choice == "1":
            modified_content = modify_content(content, "upper")
        elif choice == "2":
            modified_content = modify_content(content, "number")
        else:
            print("Invalid choice. No modification applied.")
            modified_content = content

        # Write the modified content into a new file
        output_file = "output.txt"
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"Modified content written successfully to {output_file}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. Unable to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
