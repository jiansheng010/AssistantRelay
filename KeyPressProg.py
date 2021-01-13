import keyboard

def run_keypress():
    keyboard.add_hotkey('ctrl+alt+f1', print, args=['Hello World'])

    keyboard.wait('esc')
