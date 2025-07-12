import asyncio
import os
from datetime import datetime
from everbridge import EverbridgeClient
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("EVERBRIDGE_USERNAME")
password = os.getenv("EVERBRIDGE_PASSWORD")

if not username or not password:
    raise ValueError(
        "Please set EVERBRIDGE_USERNAME and EVERBRIDGE_PASSWORD in your environment variables."
    )

client = EverbridgeClient(username=username, password=password)


async def main():
    notifications = await client.get_notifications()
    now = datetime.now()
    # simulate 2 months ago
    #now = now.replace(year=now.month - 2)
    new_notifications = [x for x in notifications if x.expiredAt > now]

    print(f"Found {len(new_notifications)} new notifications.")

    for notification in new_notifications:
        print(notification.model_dump_json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())
