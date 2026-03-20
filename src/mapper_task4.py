#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(',')
    if len(parts) <= 2:
        continue
    if parts[0] == 'ID':
        continue
    date_str = parts[2]
    year = date_str.split('/')[2].split(' ')[0]
    print(f"{year}\t1")
