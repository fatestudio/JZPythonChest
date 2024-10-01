import argparse


def remove_empty_lines(input_file, output_file):
    """
    Remove empty lines from the input file and write the non-empty lines to the output file.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
    """
    # Open the input file for reading and output file for writing
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            # Only write the line to the output file if it's not empty
            if line.strip():
                outfile.write(line)


def get_args():
    """
    Parse and return command-line arguments.

    Returns:
        argparse.Namespace: Parsed command-line arguments containing input_file and output_file paths.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_file",
        type=str,
        required=False,
        default="The REAL Reason Markelle Fultz is Still a Free Agent"
        " [English (auto-generated)] [GetSubs.cc].txt",
        help="Path to input file",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        required=False,
        default="output.txt",
        help="Path to output file",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    remove_empty_lines(args.input_file, args.output_file)
