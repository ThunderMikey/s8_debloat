#!/usr/bin/env python3
import subprocess

bloatwares = []

# read in packages to remove
for line in open('./bloatwares.txt', 'r'):
    li = line.strip()
    if not li.startswith("#"):
        bloatwares.append(li.rstrip())

def delete_bloatware(b):
    subprocess.run([
        "adb",
        "shell",
        "pm",
        "uninstall",
        "-k --user 0",
        b])

# delete bloatwares
for b in bloatwares:
    print("deleting", b)
    delete_bloatware(b)
    pass

