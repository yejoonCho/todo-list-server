from pydantic import BaseModel
from datetime import datetime


class Task(BaseModel):
    content: str