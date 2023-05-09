import subprocess
from time import sleep

with subprocess.Popen(
    ["python", "timer.py"], stdout=subprocess.PIPE,stderr=subprocess.PIPE
) as process:

    for i in process.stdout:
        print(i)
        