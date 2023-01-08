# Import the necessary modules
from PIL import ImageGrab
import pytesseract

# Take a screenshot
screenshot = ImageGrab.grab()

# Save the screenshot to a file
screenshot.save('screenshot.png')

# Use pytesseract to extract the text from the image
text = pytesseract.image_to_string(screenshot)

# Search for the word you want to find in the text
if 'word' in text:
    print('Word found in screenshot!')
else:
    print('Word not found in screenshot.')
