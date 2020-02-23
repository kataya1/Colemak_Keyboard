from pynput.keyboard import Key, Controller

keyboard = Controller()

# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
keyboard.press('a')
keyboard.release('a')

# # Type two upper case As
# keyboard.press('A')
# keyboard.release('A')
# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')

# # Type 'Hello World' using the shortcut type method
# keyboard.type('Hello World')


# monitoring

from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()


# from pynput import keyboard

# # The event listener will be running in this block
# with keyboard.Events() as events:
#     for event in events:
#         if event.key == keyboard.Key.esc:
#             break
#         else:
#             print(f'Received event {event}')

# from pynput import keyboard

# # The event listener will be running in this block
# with keyboard.Events() as events:
#     # Block at most one second
#     event = events.get(1.0)
#     if event is None:
#         print('You did not press a key within one second')
#     else:
#         print('Received event {}'.format(event))