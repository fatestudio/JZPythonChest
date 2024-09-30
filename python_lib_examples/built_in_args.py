import argparse


def get_args():
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group(title="input data")
    group.add_argument("--input",
                       type=str,
                       required=True,
                       help="Path to input JSON")
    group.add_argument(
        "--json-keys",
        nargs="+",
        default=["text"],
        help="space separate listed of keys to extract from json",
    )
    group.add_argument("--split-sentences",
                       action="store_true",
                       help="Split documents into sentences.")
    group.add_argument(
        "--keep-newlines",
        action="store_true",
        help="Keep newlines between sentences when splitting.",
    )
    return parser.parse_args()


def main():
    args = get_args()
    print(f"args: {args}")


if __name__ == "__main__":
    main()

# ➜  example git:(master) ✗ python3 built_in_args.py
# usage: built_in_args.py [-h] --input INPUT
#           [--json-keys JSON_KEYS [JSON_KEYS ...]]
#           [--split-sentences] [--keep-newlines]
# built_in_args.py: error: the following arguments are required: --input
