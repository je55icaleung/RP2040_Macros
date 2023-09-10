import time
import board
from adafruit_hid.keycode import Keycode

# colors
pink1 = 0xFF1493
pink2 = 0xFF0066
pink3 = 0xFF0080
pink4 = 0xFF3399

# keys
enter = Keycode.ENTER
ctrl = Keycode.CONTROL
cmd = Keycode.COMMAND
alt = Keycode.ALT
win = Keycode.WINDOWS
shift = Keycode.SHIFT
esc = Keycode.ESCAPE
left = Keycode.LEFT_ARROW
right = Keycode.RIGHT_ARROW

app = {
    'name' : 'Vivaldi',
    'order': 1,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (pink1, 'LINK 1 ', ['INSERT LINK\n']),
        (pink1, 'LINK 2 ', ['INSERT LINK\n']),
        (pink1, 'Outlook', ['https://outlook.office.com/mail/\n']),
        # 2nd row ----------
        (pink2, 'Book   ', [ctrl, 'b']),
        (pink2, 'Set    ', [ctrl, Keycode.F12]),
        (pink2, 'Cache  ', [ctrl, shift, Keycode.DELETE]),
        # 3rd row ----------
        (pink3, 'x Left ', [ctrl, shift, left]),
        (pink3, 'x Tabs ', [ctrl, shift, 'x']),
        (pink3, 'x Right', [ctrl, shift, right]),
        # 4th row ----------
        (pink4, '+ Tab  ', [ctrl, 't']),
        (pink4, 'x Tab  ', [ctrl, 'w']),
        (pink4, 'x Win  ', [ctrl, shift, 'w']),
    ]
}