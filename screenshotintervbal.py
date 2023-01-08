# Import the necessary modules
from PIL import ImageGrab
import time
import pytesseract



for i in range(5):
    print("Snapped")
    screenshot = ImageGrab.grab()
    text = pytesseract.image_to_string(screenshot)
    if 'Log In' or 'Sign in' in text:
        print('Word found in screenshot!')
        screenshot.save('screenshot.png')
    time.sleep(1)

# Take a screenshot

# Save the screenshot to a file

