import asyncio

import aiohttp


async def fetch_url(session, url):
    """
    Asynchronously fetch data from a URL.

    Args:
        session (aiohttp.ClientSession): The active session used for making requests.
        url (str): The URL to fetch data from.

    Returns:
        str: The content retrieved from the URL.
    """
    async with session.get(url) as response:
        print(f"Fetching data from {url}")
        data = await response.text()  # await for the I/O operation to complete
        print(f"Data received from {url}: {len(data)} characters")
        return data


async def main():
    """
    Main function to concurrently fetch data from multiple URLs using aiohttp and asyncio.
    """
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)  # Run all tasks concurrently


if __name__ == '__main__':
    # Run the main function
    asyncio.run(main())
