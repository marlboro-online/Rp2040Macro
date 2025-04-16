from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Medibang-Control 1',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Flip', [Keycode.UP_ARROW]), ##flips the canvas
        (0x004000, 'Grid', [Keycode.CONTROL, Keycode.G]), ##brings up the grid
        (0x000040, 'D color', [Keycode.D]), ##swaps the primary colours and secondary to colours to black and white
        # 2nd row ----------
        (0x101010, 'Br -', [Keycode.LEFT_BRACKET]), ##Makes the brush smaller
        (0x101010, 'Br +', [Keycode.RIGHT_BRACKET]), ##Makes the brush bigger
        (0x000040, 'Delete', [Keycode.DELETE]), ##Delete everything in the layer
        # 3rd row ----------
        (0x101010, 'L Shift', [Keycode.SHIFT]), ##shift for navigation
        (0x101010, 'Undo', [Keycode.CONTROL, Keycode.Z]), ## Simple Ctrl + Z to undo changes
        (0x000040, 'Eraser', [Keycode.E]), ##swap to eraser
        # 4th row ----------
        (0x101010, 'L CTRL', [Keycode.CONTROL]), ##Ctrl for navigation
        (0x101010, 'Space', [Keycode.SPACE]), ## Space for Navigate, combine with shift to tilt, ctrl to zoom
        (0x000040, 'Brush', [Keycode.B]), ##swap to brush tool
    ]
}