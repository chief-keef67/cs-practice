from collections import Counter

LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}

def parse_event(line: str) -> dict:
    parts = line.split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Частей строки больше 3")

    time, level, message = parts

    if level not in LEVELS or not message.strip():
        raise ValueError("Сообщение отсутствует или неверный уровень")

    return {
        "time": time,
        "level": level,
        "message": message,
    }

def count_levels(lines) -> dict:
    counts = Counter()

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] += 1
        else:
            counts[event["level"]] += 1

    return dict(counts)
