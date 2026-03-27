from pydantic import BaseModel


class Trainer(BaseModel):
    trainer_id: str
    name: str
