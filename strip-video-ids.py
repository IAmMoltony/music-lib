#!/usr/bin/python3

import os, re

print("music-lib Strip Video IDs 1.0")

pattern = re.compile(r'^(.*?)(\[[a-zA-Z0-9\-_]{11})\.*')

for filename in os.listdir("."):
    m = pattern.match(filename)
    if m:
        name = m.group(1).strip()
        _, ext = os.path.splitext(filename)
        new_name = f"{name}{ext}"
        print(f"{filename} -> {new_name}")
        os.rename(filename, new_name)