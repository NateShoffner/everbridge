
import asyncio
import os
from datetime import datetime
from everbridge import EverbridgeClient
from dotenv import load_dotenv

load_dotenv()

client = EverbridgeClient(username=os.getenv("EVERBRIDGE_USERNAME"),
                          password=os.getenv("EVERBRIDGE_PASSWORD"))

async def main():
    notifications = await client.get_notifications()
    now = datetime.now()
    for notification in notifications:
        # print the notification id, title, and body
        # also the timeit was created in human readable format,
        is_expired = notification.expiredAt <= now
        if is_expired:
            print(f"{notification.id}: {notification.title} - (EXPIRED)")
        else:
            print(f"{notification.id}: {notification.title} - {notification.body}")

        #details = await client.get_notification(notification.id)
        #print(details)

if __name__ == "__main__":
    asyncio.run(main())