import time
import board
from adafruit_hid.keycode import Keycode

# colors
darkOrange = 0xFF9933
lightOrange = 0xFFAB40
lightBlue = 0x99FFFF
darkBlue = 0x004166

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
    'name' : 'Windows Home',
    'order': 0,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (darkOrange, 'ScrSh  ', [win, shift, 's']),
        (darkOrange, 'Zones  ', [alt, shift, 'w']),
        (darkOrange, 'Focus  ', [win, ctrl, 't']),
        # 2nd row ----------
        (lightOrange, 'Term   ', [ctrl, alt, 't']),
        (lightOrange, 'Exp    ', [ctrl, 'e']),
        (lightOrange, 'Task   ', [ctrl, shift, esc]),
        # 3rd row ----------
        (lightBlue, 'Viv    ', [ctrl, alt, 'v']),
        (lightBlue, 'Disc   ', [ctrl, alt, 'd']),
        (lightBlue, 'Spotify', [cmd, alt, 's']),
        # 4th row ----------
        (darkBlue, 'L Desk ', [win, ctrl, left]),
        (darkBlue, 'R Desk ', [win, ctrl, right]),
        (darkBlue, 'Lang   ', [shift, alt]),
    ]
}
