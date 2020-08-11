import keyboard

active_keys: list = []


def keys_pressed():
    global active_keys
    temp = []
    for key in active_keys:
        if keyboard.is_pressed(key):
            temp.append(key)

    active_keys = temp


def key_pressed_event(event):
    key = event.name
    if key not in active_keys:
        active_keys.append(key)

    keys_pressed()


keyboard.on_press(callback=key_pressed_event)


class Controller:
    def __init__(self):
        self.active_keys = []

        # Digital Pad
        self.up = '8'
        self.left = '4'
        self.right = '6'
        self.down = '2'

        # Buttons
        self.start = 'enter'  # Number pad enter
        self.a = 'x'
        self.b = 'c'
        self.l_trigger = 'q'
        self.r_trigger = 'e'
        self.z_trigger = 'space'

        # C Buttons
        self.c_up = 'w'
        self.c_left = 'a'
        self.c_right = 'd'
        self.c_down = 's'

        # Analog Stick
        self.analog_up = 'up'
        self.analog_left = 'left'
        self.analog_right = 'right'
        self.analog_down = 'down'

    def get_active_keys(self):
        self.active_keys = active_keys
        return self.active_keys
