import os
import requests
import subprocess
import signal


URL = "http://do.n-konovalov.ru:5020/get"
PID = None


def fetch_state():
    resp = requests.get(URL)
    content = resp.content
    print "got resp status %s" % content
    return bool(content)


def main_loop():
    global PID
    while True:
        state = fetch_state()
        if state:
            # Start BOINC by killing process
            print "stopping"
            if PID:
                print "pid %s" % PID
                os.kill(PID, signal.SIGTERM)
        else:
            # Stop BOINC by starting process
            print "starting"
            PID = subprocess.Popen(("/env/bin/python", "stopper.py")).pid
            print "started pid %s" % PID


def check_existing_pid():
    pass


if __name__ == "__main__":
    check_existing_pid()
    main_loop()
