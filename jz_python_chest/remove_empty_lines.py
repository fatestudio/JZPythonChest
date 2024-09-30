import argparse


def remove_empty_lines(input_file, output_file):
    # Open the input file for reading and output file for writing
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            # Only write the line to the output file if it's not empty
            if line.strip():
                outfile.write(line)


def get_args():
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
