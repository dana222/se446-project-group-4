#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    
    if not line:
        continue

    parts = line.split(',')

    # skip header or bad lines
    if len(parts) <= 8:
        continue

    if parts[0] == "ID":
        continue

    arrest = parts[8].strip().lower()

    # handle variations like True/False, TRUE, etc.
    if arrest == "true" or arrest == "false":
        print(f"{arrest}\t1")
