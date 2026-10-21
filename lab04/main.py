import sys

from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
print(lines)
records = read_valid(lines)
invalid_count = 0
for line in lines:
    if not line.strip():
        continue
    try:
        parse_record(line)
    except ValueError:
        invalid_count += 1
print(len(records))
print(invalid_count)
city = warmest_city(records)
if city:
    averages = average_by_city(records)
    print(f'{averages[city]:.1f}')
else:
    print("0.0")