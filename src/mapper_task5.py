#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(',')
    if len(parts) <= 8:
        continue
    if parts[0] == 'ID':
        continue
    arrest = parts[9].lower().strip()
    if arrest in ('true', 'false'):
        print(f"{arrest}\t1")
