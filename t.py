import subprocess
import sys

with open("test.log", "wb") as f:
    process = subprocess.Popen(["python3", "timer.py"], stdout=subprocess.PIPE)
    for c in iter(lambda: process.stdout.read(1), b""):
        sys.stdout.buffer.write(c)
        # f.buffer.write(c)
        print(c)
