from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillOut

router = APIRouter(prefix="/skills", tags=["Skills"])

@router.put("/{skill_id}", response_model=SkillOut)
def update_skill(
    skill_id: int,
    skill: SkillCreate,
    db: Session = Depends(get_db)
):
    db_skill = db.query(Skill).filter(Skill.id == skill_id).first()
    if not db_skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    db_skill.name = skill.name
    db_skill.level = skill.level
    db_skill.learned_date = skill.learned_date

    db.commit()
    db.refresh(db_skill)
    return db_skill
