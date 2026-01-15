from datetime import date
from sqlalchemy.orm import Session
from app.models.skill_history import SkillHistory
from app.models.skill import Skill
from app.core.decay_engine import compute_decay_score

def recalculate_skill_decay(skill: Skill, db: Session):
    history = (
        db.query(SkillHistory)
        .filter(SkillHistory.skill_id == skill.id)
        .order_by(SkillHistory.date)
        .all()
    )

    if not history:
        return 0.0

    # ✅ Safe handling when skill was never used
    used_dates = [h.date for h in history if h.usage == 1]

    if used_dates:
        last_used = max(used_dates)
        days_since = (date.today() - last_used).days
    else:
        # never used → maximum decay
        days_since = (date.today() - history[0].date).days

    usage_freq = sum(h.usage for h in history) / len(history)

    score = compute_decay_score(days_since, usage_freq, skill.level)

    # ✅ Update ALL rows so decay curve works
    for h in history:
        days_since = (date.today() - h.date).days
        h.decay_score = compute_decay_score(
           days_since,
           usage_freq,
           skill.level
    )

    db.commit()
    return round(score, 2)
