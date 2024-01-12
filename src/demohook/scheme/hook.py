from datetime import datetime

from pydantic import BaseModel, Field, model_validator


class HookDemo(BaseModel):
    id : str = ""
    name: str = Field(..., title="名称")
    age: int = Field(..., title="年龄")
    timestamp: int = 0

    @model_validator(mode='after')
    def update_id_and_ts(self):
        timestring = self.name
        ts = int(datetime.strptime(timestring, "%Y-%m-%d %H:%M:%S").timestamp())

        id = f"{self.name}_{self.age}_{ts}"
        self.id = id
        self.timestamp = ts

        return self