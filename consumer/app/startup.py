import subprocess, time, sys
from stream import consume_loop

def ping_until_up(target="172.22.0.4"):
    while True:
        status = subprocess.run(["ping", "-c", "3", target], capture_output=True)
        if status.returncode == 0:
            return
        print("Target is not up yet. Sleeping for 5 seconds.")
        time.sleep(5)

print("Starting... Beginning to ping the target.")
ping_until_up()
print("Target responsive, begin basic consume loop with topics")
consume_loop(["database"])