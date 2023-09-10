import time
import keyfactory
from adafruit_macropad import MacroPad
from app import App
from display import Display
from pixels import Pixels

MACRO_FOLDER = '/macros'

macropad = MacroPad()
screen = Display(macropad)
pixels = Pixels(macropad)
last_position = None
leds_off = False  
app_index = 0

screen.initialize()
apps = App.load_all(MACRO_FOLDER)

if not apps:
    screen.setTitle('NO MACRO FILES FOUND')
    while True:
        pass

try: 
    macropad.keyboard.release_all()
except OSError as err:
    print(err)
    screen.setTitle('NO USB CONNECTION')
    while True:
        pass

while True:
    position = macropad.encoder
    if position != last_position:
        last_position = position
        app_index = position % len(apps)
        macropad.keyboard.release_all()
        screen.setApp(apps[app_index])
        pixels.setApp(apps[app_index])

    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed

    if encoder_switch:
        leds_off = not leds_off

    if leds_off:
        pixels.sleep()
    else:
        pixels.resume()

    event = macropad.keys.events.get()
    if not event or event.key_number >= len(apps[app_index].macros):
        continue

    key_number = event.key_number
    pressed = event.pressed

    sequence = apps[app_index].macros[key_number][2] if key_number < 12 else []
    if pressed:
        if key_number < 12:
            pixels.highlight(key_number, 0xFFFFFF)
        for item in sequence:
            keyfactory.get(item).press(macropad)
    else:
        for item in sequence:
            keyfactory.get(item).release(macropad)
        if key_number < 12:
            pixels.reset(key_number)
