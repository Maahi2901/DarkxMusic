

import asyncio

from pyrogram import Client


print("π΄π½ππ΄π ππΎππ π°πΏπΏ πΈπ½π΅πΎππΌπ°ππΈπΎπ½ π΅ππΎπΌ my.telegram.org/apps π±π΄π»πΎπ.")


async def main():
    async with Client(":memory:", api_id=int(input("API ID:")), api_hash=input("API HASH:")) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
