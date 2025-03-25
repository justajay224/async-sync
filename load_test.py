import asyncio
import time
import httpx
from dotenv import load_dotenv
import os

load_dotenv()

async def make_async_request(client, url):
    response = await client.get(url)
    return response.status_code

async def main_async(url, requests=100):
    timeout = httpx.Timeout(timeout=30.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        start = time.time()
        tasks = [make_async_request(client, url) for _ in range(requests)]
        results = await asyncio.gather(*tasks)
        duration = time.time() - start
        print(f"Async - Total time: {duration:.2f}s")
        print(f"Async - Requests/s: {requests/duration:.2f}")

def main_sync(url, requests=100):
    with httpx.Client() as client:
        start = time.time()
        for _ in range(requests):
            client.get(url)
        duration = time.time() - start
        print(f"Sync - Total time: {duration:.2f}s")
        print(f"Sync - Requests/s: {requests/duration:.2f}")

if __name__ == "__main__":
    url_async = os.getenv('url_async')
    url_sync = os.getenv('url_sync')
    
    print("Testing Async Endpoint:")
    asyncio.run(main_async(url_async))
    
    print("\nTesting Sync Endpoint:")
    main_sync(url_sync)