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

def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_list = None

    def convert_value(value):
        value = value.strip()

        if value.isdigit() or (
            value.startswith("-") and value[1:].isdigit()
        ):
            return int(value)

        try:
            if "." in value:
                return float(value)
        except ValueError:
            pass

        if value.lower() in ("true", "yes"):
            return True

        if value.lower() in ("false", "no"):
            return False

        return value

    for line in lines:
        line = line.split("#")[0].rstrip()

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