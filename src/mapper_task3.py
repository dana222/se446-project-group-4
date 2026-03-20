#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(',')
    if len(parts) <= 7:
        continue
    if parts[0] == 'ID':
        continue
    location = parts[7]
    print(f"{location}\t1")
# Mapper for Task 3 - Location Hotspots - Sema Raslan
