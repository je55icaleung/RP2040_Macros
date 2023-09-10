from adafruit_hid.keycode import Keycode

# colors
off = 0x000000

app = {
    'name' : 'Numpad',
    'order': 2,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (off, '7    ', ['7']),
        (off, '8    ', ['8']),
        (off, '9    ', ['9']),
        # 2nd row ----------
        (off, '4    ', ['4']),
        (off, '5    ', ['5']),
        (off, '6    ', ['6']),
        # 3rd row ----------
        (off, '1    ', ['1']),
        (off, '2    ', ['2']),
        (off, '3    ', ['3']),
        # 4th row ----------
        (off, '0    ', ['0']),
        (off, '.    ', [Keycode.BACKSPACE]),
        (off, 'ENTER', [Keycode.ENTER])
    ]
}
