print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
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
keyboard.SCL=board.D5
keyboard.SDA=board.D4

oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["Numpad", "Fn"]},
        corner_three={0:OledReactionType.STATIC,1:[""]},
        corner_four={0:OledReactionType.STATIC,1:[""]},
        ),
        toDisplay=OledDisplayMode.TXT,flip=False)

keyboard.extensions.append(oled_ext)

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
    