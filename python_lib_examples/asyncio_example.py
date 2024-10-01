import asyncio


async def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        await asyncio.sleep(1)  # Simulate I/O delay


async def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        await asyncio.sleep(1.5)  # Different I/O delay


async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())

    await task1
    await task2


if __name__ == '__main__':
    # Start the event loop
    asyncio.run(main())
