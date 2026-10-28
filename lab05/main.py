from pathlib import Path

from logstats import count_levels, top_errors, format_report


def main():
    filename = input().strip()
    log_path = Path(filename)

    with open(log_path, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(log_path, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    broken = counts.get("BROKEN", 0)
    error_count = counts.get("ERROR", 0)

    total = sum(counts.values())

    print(total)
    print(error_count)
    print(broken)

    report = format_report(counts, errors)
    report_path = Path(__file__).resolve().parent / "report.txt"

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)


if __name__ == "__main__":
    main()