import subprocess
import time

while True:
    # Get a list of running processes
    proc_list = subprocess.check_output(['tasklist']).decode('utf-8').split('\n')
    # Check if a browser process is running
    for proc in proc_list:
        if 'chrome.exe' in proc:
            print('NOW')
            break
    # Wait for 1 second before checking again
    time.sleep(1)