import json


def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().splitlines()

    if not lines:
        return []

    headers = lines[0].split(",")
    records = []

    for line in lines[1:]:
        if not line:
            continue

        values = line.split(",")
        record = dict(zip(headers, values))
        records.append(record)

    return records