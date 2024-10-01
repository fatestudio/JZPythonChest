import asyncio
from concurrent.futures import ThreadPoolExecutor

# Define an executor for running blocking I/O in a thread
executor = ThreadPoolExecutor()


# Asynchronous function to read a file
async def async_read_file(file_path):
    loop = asyncio.get_running_loop()

    # Use run_in_executor to run the blocking I/O operation in a separate thread
    with open(file_path, 'r') as file:
        return await loop.run_in_executor(executor, file.read)


# Asynchronous function to write to a file
async def async_write_file(file_path, content):
    loop = asyncio.get_running_loop()

    # Use run_in_executor to run the blocking I/O operation in a separate thread
    with open(file_path, 'w') as file:
        return await loop.run_in_executor(executor, file.write, content)


# Testing the async file I/O functions
async def main():
    # Writing to a file
    await async_write_file('example.txt', 'Hello, Async World!')
    print("File written successfully!")

    # Reading from a file
    content = await async_read_file('example.txt')
    print(f"File content: {content}")


if __name__ == '__main__':
    # Run the main function
    asyncio.run(main())
