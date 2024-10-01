import asyncio

import aiofiles


async def read_file_lines(filepath):
    """
    Asynchronous generator function to read a file line by line.

    Args:
        filepath (str): The path to the file to read.

    Yields:
        str: Each line of the file stripped of leading/trailing whitespace.
    """
    async with aiofiles.open(filepath, mode='r') as file:
        async for line in file:
            yield line.strip()  # Yield each line asynchronously


async def main():
    """
    Example usage of the read_file_lines function.
    Reads and prints each line from the specified file.
    """
    async for line in read_file_lines("file1.txt"):
        print(f"Read line: {line}")


if __name__ == '__main__':
    # Running the asynchronous main function
    asyncio.run(main())
