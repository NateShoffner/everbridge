# Everbridge Python Wrapper

[![Python package](https://github.com/NateShoffner/everbridge/actions/workflows/python-package.yml/badge.svg)](https://github.com/NateShoffner/everbridge/actions/workflows/python-package.yml)

[![PyPI - Version](https://img.shields.io/pypi/v/everbridge)](https://pypi.org/project/everbridge/)




Python wrapper for the Everbridge service.

Currently, the library uses password-based authentication.

wip

## Example Usage

```python

import asyncio
import os
from everbridge import EverbridgeClient
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("EVERBRIDGE_USERNAME")
password = os.getenv("EVERBRIDGE_PASSWORD")

client = EverbridgeClient(username=username, password=password)

async def main():
    notifications = await client.get_notifications()

    print(f"Found {len(notifications)} notifications.")

    for notification in notifications:
        print(notification.id, notification.title)


if __name__ == "__main__":
    asyncio.run(main())

```
