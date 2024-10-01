if __name__ == '__main__':
    from pathlib import Path

    # better than os and os.path
    # 1. Create a Path object
    path = Path("example_directory/example.txt")

    # 2. Check if the file or directory exists
    print(f"Does the path exist? {path.exists()}")

    # 3. Create a new directory (parents=True creates any missing parent
    # directories)
    path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Created directory: {path.parent}")

    # 4. Write text to a file
    path.write_text("Hello, pathlib!")
    print(f"Written to file: {path}")

    # 5. Read text from a file
    content = path.read_text()
    print(f"Content of file: {content}")

    # 6. Rename the file
    new_path = path.with_name("example_renamed.txt")
    path.rename(new_path)
    print(f"Renamed file to: {new_path}")

    # 7. Check file properties
    print(f"Is it a file? {new_path.is_file()}")
    print(f"File size: {new_path.stat().st_size} bytes")

    # 8. Iterate over all text files in the directory
    print("All text files in the directory:")
    for text_file in new_path.parent.glob("*.txt"):
        print(text_file)

    # 9. Delete the file
    new_path.unlink()
    print(f"Deleted file: {new_path}")

    # 10. Remove the directory if it's empty
    new_path.parent.rmdir()
    print(f"Deleted directory: {new_path.parent}")
