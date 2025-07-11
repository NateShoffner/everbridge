import aiohttp

from .models import Notification

BASE_URL = "https://api.everbridge.net/digitalapps/v2"

class EverbridgeClient:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.refresh_token = None
        self.access_token = None
        self.expires_at = None

    async def get_access_token(self):
        url = f"{BASE_URL}/authorizations/oauth2/token"

        headers = {
            "accept": "application/json",
        }

        payload = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=payload) as response:
                r_json = await response.json()


        print(r_json)

        return r_json
    
    async def get_notifications(self):
        """ Get all notifications """
        r_json = await self.get_access_token()
        
        access_token = r_json['accessToken']
        client_id = r_json['clientId']

        url = f"{BASE_URL}/notifications/messages"

        headers = {
            "accept": "application/json",
            "Authorization": "token " + access_token['value'],
            "Client-Id": client_id,
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r_json = await response.json()

        notifications = [Notification(**item) for item in r_json]

        return notifications
    
    async def get_notification(self, notification_id: str):
        """ Get a single notification by its ID """
        r_json = await self.get_access_token()
        
        access_token = r_json['accessToken']
        client_id = r_json['clientId']

        url = f"{BASE_URL}/notifications/messages/{notification_id}"

        headers = {
            "accept": "application/json",
            "Authorization": "token " + access_token['value'],
            "Client-Id": client_id,
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r_json = await response.json()

        notification = Notification(**r_json)

        return notification
    
    async def get_events(self):
        """ Get all events """
        r_json = await self.get_access_token()
        
        access_token = r_json['accessToken']
        client_id = r_json['clientId']

        url = f"{BASE_URL}/events"

        headers = {
            "accept": "application/json",
            "Authorization": "token " + access_token['value'],
            "Client-Id": client_id,
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                r_json = await response.json()

        return r_json