import random
from database import get_last_index, update_last_index

MOTIVATIONAL_DATA = [
    {"title": "Stay Focused", "msg": "Discipline is choosing between what you want now and what you want most."},
    {"title": "Keep Going", "msg": "The only way to do great work is to love what you do."},
    {"title": "Mindset", "msg": "Your mind is a powerful thing. When you fill it with positive thoughts, your life will start to change."},
    {"title": "Consistency", "msg": "Small daily improvements over time lead to stunning results."},
    {"title": "Resilience", "msg": "Failure is not the opposite of success; it is part of success."},
    {"title": "Action", "msg": "Don't wait for opportunity. Create it."},
    {"title": "Growth", "msg": "Comfort zones are plush, but nothing ever grows there."},
    {"title": "Persistence", "msg": "It does not matter how slowly you go as long as you do not stop."},
]

def get_next_quote():
    last_idx = get_last_index()
    next_idx = (last_idx + 1) % len(MOTIVATIONAL_DATA)
    update_last_index(next_idx)
    
    item = MOTIVATIONAL_DATA[next_idx]
    return f"💡 **{item['title']}**\n\n{item['msg']}\n\nKeep going 🚀"

def get_random_quote():
    # Used for the /motivate command
    item = random.choice(MOTIVATIONAL_DATA)
    return f"💡 **{item['title']}**\n\n{item['msg']}\n\nKeep going 🚀"
