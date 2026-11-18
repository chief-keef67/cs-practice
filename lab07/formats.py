import json


def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().splitlines()

    if not lines:
        return []

    headers = [item.strip() for item in lines[0].split(",")]
    records = []

    for line in lines[1:]:
        if not line.strip():
            continue

        values = [item.strip() for item in line.split(",")]
        record = dict(zip(headers, values))
        records.append(record)

    return records

def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_list = None

    def convert_value(value):
        value = value.strip()

        if value.lower() in ("true", "yes"):
            return True

        if value.lower() in ("false", "no"):
            return False

        try:
            return int(value)
        except ValueError:
            pass

        try:
            return float(value.replace(",", "."))
        except ValueError:
            return value

    for line in lines:
        line = line.split("#", 1)[0].rstrip()

        if not line.strip():
            continue

        stripped = line.strip()

        if stripped.startswith("- "):
            if current_list is not None:
                settings[current_list].append(
                    convert_value(stripped[2:])
                )
            continue

        if ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()

            if value == "":
                settings[key] = []
                current_list = key
            else:
                settings[key] = convert_value(value)
                current_list = None

    return settings

def merge_by_key(
    rows: list[dict],
    extra: dict,
    key: str = "id"
) -> list[dict]:
    result = []

    for row in rows:
        record = dict(extra.get(str(row.get(key)), {}))
        record.update(row)
        result.append(record)

    return result

def records_to_json(records: list[dict]) -> str:
    return json.dumps(
        records,
        ensure_ascii=False,
        indent=2,
        sort_keys=True
    )