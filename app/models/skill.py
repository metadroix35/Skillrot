from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.models.base import Base

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    learned_date = Column(Date, nullable=False)
