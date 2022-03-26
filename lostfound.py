from pynput.keyboard import KeyCode, Listener, Key
from PIL import ImageGrab
import time
from time import localtime, strftime

def on_press(key):
    pass

def on_release(key):
    if key == KeyCode.from_char('e'):
        time.sleep(1)
        filepath = strftime("%Y-%m-%d %H-%M-%S", localtime())
        filepath = filepath + ".png"
        screenshot = ImageGrab.grab()
        screenshot.save(filepath, 'PNG')
    elif key == Key.f12:
        return False

# Collect events until released

try:
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    pass