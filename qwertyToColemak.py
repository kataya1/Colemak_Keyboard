# from pynput.keyboard import Key, Controller
import pynput

# qwertyuiopasdfghjkl;zxcvbnm
# qwfpgjluy;arstdhneiozxcvbkm
qtoc = {'q': 'q',
        'w': 'w',
        'e': 'f',
        'r': 'p', 
        't': 'g', 
        'y': 'j', 
        'u': 'l', 
        'i': 'u', 
        'o': 'y', 
        'p': ';', 
        'a': 'a',
        's': 'r',
        'd': 's',
        'f': 't',
        'g': 'd',
        'h': 'h',
        'j': 'n',
        'k': 'e',
        'l': 'i',
        ';': 'o',
        'z': 'z',
        'x': 'x',
        'c': 'c',
        'v': 'v',
        'b': 'b',
        'n': 'k',
        'm': 'm'}

cont = pynput.keyboard.Controller()
def on_press(key):
    try:
        # print(qtoc[key.char])
        cont.press(qtoc[key.char])
        cont.press(qtoc[key.char])
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    # print('{0} released'.format(key))
    # cont.release(key.char)
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
# with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
listener = pynput.keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
