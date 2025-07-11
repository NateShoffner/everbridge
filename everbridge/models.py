from pydantic import BaseModel, validator
from datetime import datetime


class Sender(BaseModel):
    id: str


class Setting(BaseModel):
    requestImage: bool
    requestLocation: bool
    requestComment: bool
    allowShare: bool
    requireConfirm: bool


class State(BaseModel):
    read: bool
    shared: bool
    confirmed: bool
    active: bool


class Notification(BaseModel):
    id: str
    title: str
    body: str
    priority: bool
    sender: Sender
    source: str
    setting: Setting
    state: State
    enableIncidentChat: bool
    ittl: bool
    createdAt: datetime
    expiredAt: datetime

    @validator('createdAt', 'expiredAt', pre=True)
    def convert_timestamp_to_datetime(cls, value):
        return datetime.fromtimestamp(value / 1000)