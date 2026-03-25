#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

for parts in reader:
    if not parts:
        continue
    if parts[0] == 'ID':
        continue
    if len(parts) <= 7:
        continue

    location = parts[7].strip()
    if location:
        print(f"{location}\t1")
