from adafruit_hid.keycode import Keycode

app = {
    'name' : 'imovie shortcuts',
    'macros' : [
        # COLOR(in 0x+hexcode,    'LABEL',    'KEY SEQUENCE'
        # 1st row ----------
        (0xff0000, 'SP Audio', [Keycode.OPTION, Keycode.COMMAND, 'B']), ## separates audio from the clip
        (0xff0000, 'Split', [Keycode.COMMAND, 'B']), ##splits the clip at the play head
        (0xff0000, 'Combine', [Keycode.SHIFT, Keycode.COMMAND, 'B']), ##combines selected clips
        # 2nd row ----------
        (0xff0000, 'Undo', [Keycode.COMMAND, 'Z']), ##undo changes
        (0xff0000, 'UP', [Keycode.UP_ARROW]),## Navigation but on clips, go to the beginning of the clip
        (0xff0000, 'Redo', [Keycode.SHIFT, Keycode.COMMAND,'Z']),
        # 3rd row ----------
        (0xff0000, 'Left', [Keycode.LEFT_ARROW]), ##Move back one frame
        (0xff0000, 'Down', [Keycode.DOWN_ARROW]), ##Navigation but on clips, go to the end of the clip
        (0xff0000, 'Right', [Keycode.RIGHT_ARROW]), ##Move forward one frame
        # 4th row ----------
        (0xff0000, 'CL Start', ['i']), ##go to the start of a selected clip
        (0xff0000, 'Cut', ['x']), ## cut / delete selection
        (0xff0000, 'CL End', ['o']), ##go to the end of a selected clip
    ]
}