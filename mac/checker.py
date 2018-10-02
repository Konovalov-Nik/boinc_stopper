import os
import requests
import subprocess
import signal
import time


URL = "http://do2.n-konovalov.ru:5020/get"
PID = None


def fetch_state():
    resp = requests.get(URL)
    content = resp.content
    print "got content %s" % content
    if content in ("True", "true", "1", "yes", "enabled"):
        state = True
    else:
        state = False
    print "got resp status %s" % state
    return state


def main_loop():
    global PID
    proc = None
    while True:
        state = fetch_state()
        if not state:
            # Start BOINC by killing process
            print "stopping"
            if PID:
                print "pid %s" % PID
                proc.kill()
                proc.communicate()
            PID = None
        else:
            # Stop BOINC by starting process
            if PID is not None:
                print "already running"
                time.sleep(10)
                continue

            print "starting"
            cwd = os.getcwd()
            proc = subprocess.Popen((cwd + "/stopper"), stdout=subprocess.PIPE, shell=True)
            PID = proc.pid
            print "started pid %s" % PID

        time.sleep(10)


def check_existing_pid():
    pass


if __name__ == "__main__":
    check_existing_pid()
    main_loop()
