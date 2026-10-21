import sys

def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("В записи не ровно три данных")
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    if not city or not date:
        raise ValueError("Город или дата пустые")
    try:
        temp = float(temp_str)
    except ValueError:
        print("Температура не является числом")
    return city, temp, date

def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
        except ValueError:
            continue
        records.append(record)
    return records