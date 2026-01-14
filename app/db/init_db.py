from app.db.database import engine
from app.models.base import Base
from app.models import user, skill, skill_history

def init_db():
    Base.metadata.create_all(bind=engine)
