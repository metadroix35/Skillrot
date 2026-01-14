from pydantic import BaseModel
from datetime import date

class SkillCreate(BaseModel):
    user_id: int
    name: str
    level: str
    learned_date: date

class SkillOut(SkillCreate):
    id: int

    class Config:
        from_mode = True
