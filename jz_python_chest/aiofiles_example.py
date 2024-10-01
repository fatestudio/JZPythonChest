import asyncio

import aiofiles


async def read_file(filepath):
    """
    Asynchronous read a file
    """
    async with aiofiles.open(filepath, mode='r') as file:
        content = await file.read()
        print(f"Content from {filepath}:")
        print(content)


async def main():
    tasks = [read_file('file1.txt'), read_file('file2.txt')]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
