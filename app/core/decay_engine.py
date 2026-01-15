from datetime import date

BASE_DECAY_RATE = 0.015  # tunable constant
MAX_DECAY_DAYS = 90     # 🔒 prevents irreversible decay

def compute_decay_score(
    days_since_last_use: int,
    usage_frequency: float,
    skill_level: str
) -> float:
    """
    Returns skill health percentage (0–100)
    """

    level_factor = {
        "beginner": 1.2,
        "intermediate": 1.0,
        "advanced": 0.8
    }.get(skill_level.lower(), 1.0)
    
     # 🔒 cap decay window
    effective_days = min(days_since_last_use, MAX_DECAY_DAYS)

    decay = days_since_last_use * BASE_DECAY_RATE * level_factor
    recovery = usage_frequency * 0.5

    score = 100 - (decay * 100) + (recovery * 10)

    return max(0, min(100, round(score, 2)))
