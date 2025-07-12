from pydantic import BaseModel, field_validator
from datetime import datetime


class Sender(BaseModel):
    id: int


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
    id: int
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

    @field_validator("createdAt", "expiredAt", mode="before")
    def convert_timestamp_to_datetime(cls, value):
        return datetime.fromtimestamp(value / 1000)
