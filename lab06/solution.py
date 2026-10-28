def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        ext = name.rsplit(".", 1)[-1].lower() if "." in name else ""
        result[ext] = result.get(ext, 0) + 1
    return result

def deepest_path(paths: list[str]) -> str:
    return min(paths, key=lambda p: (-p.count("/"), p)) if paths else ""

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = n_bytes
    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size} {unit}" if unit == "Б" else f"{size:.1f} {unit}"
        size /= 1024