#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(',')
    if len(parts) <= 5:
        continue
    if parts[0] == 'ID':
        continue
    crime_type = parts[5]
    print(f"{crime_type}\t1")
