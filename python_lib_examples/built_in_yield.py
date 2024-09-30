def read_file_line_by_line(file_name):
    with open(file_name) as file:
        for line in file:
            yield line.strip()


if __name__ == "__main__":
    for line in read_file_line_by_line("built_in_yield.txt"):
        print(line)
