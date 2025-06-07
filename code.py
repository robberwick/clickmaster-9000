print("Starting")

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.rgb import AnimationModes
from kmk.extensions.RGB import RGB


keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D8, board.D7, board.D6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.clear()
keyboard.extensions.append(MediaKeys())

# Regular GPIO Encoder
encoder_handler.pins = (
    # regular direction encoder and no button
    (board.D9, board.D10, None),  
)

# OLED display
i2c_bus = busio.I2C(board.D5, board.D4)

driver = SSD1306(i2c=i2c_bus)
display = Display(
    display=driver,
    dim_time=20, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=60, # time in seconds to turn off screen
    powersave_dim_time=10, # time in seconds to reduce screen brightness
    powersave_dim_target=0.1, # set level for brightness decrease
    powersave_off_time=30, # time in seconds to turn off screen
)
display.entries = [
    TextEntry(text='Layer: ', x=0, y=32, y_anchor='B'),
    TextEntry(text='BASE', x=40, y=32, y_anchor='B', layer=0),
    TextEntry(text='NUM', x=40, y=32, y_anchor='B', layer=1),
    TextEntry(text='NAV', x=40, y=32, y_anchor='B', layer=2),
    TextEntry(text='0 1 2', x=0, y=4),
    TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
    TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
    TextEntry(text='2', x=24, y=4, inverted=True, layer=2),   
]

keyboard.extensions.append(display)

# LEDs
rgb = RGB(pixel_pin=board.NEOPIXEL, num_pixels=1, val_limit=255, val_step=2, val_default=255,
        hue_step=5,
        hue_default=0,
        sat_step=5,
        sat_default=255,
        rgb_order=(1, 0, 2),
        animation_speed=1,
        breathe_center=1,  # 1.0-2.7a
        knight_effect_length=3,
        animation_mode=AnimationModes.STATIC,
        reverse_animation=False,
        refresh_rate=60,)

keyboard.extensions.append(rgb)

#Layer keys
LAYER_TAP = KC.LT(1, KC.PENT, prefer_hold=True, tap_interrupted=False, tap_time=250) # any tap longer than 250ms will be interpreted as a hold

keyboard.keymap = [
    # Base layer - numpad
    [
        KC.P7, KC.P8, KC.P9,
        KC.P4, KC.P5, KC.P6,
        KC.P1, KC.P2, KC.P3,
        KC.RGB_TOG, KC.P0, LAYER_TAP
    ],
    #
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I,
        KC.J, KC.K, KC.TRNS
    ],
]

encoder_handler.map = [
    (( KC.VOLU, KC.VOLD, KC.NO), ), # Layer 0
    (( KC.RGB_HUI, KC.RGB_HUD, KC.NO), ), # Layer 1
]
if __name__ == '__main__':
    keyboard.go()
 