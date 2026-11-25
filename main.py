import os

LINE = "I hired a life coach, and after one session he asked if I knew anyone hiring life coaches."

assert 1 <= len(LINE) <= 200, "gate: entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
