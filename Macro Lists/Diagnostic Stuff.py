from adafruit_hid.keycode import Keycode

app = {
    'name' : 'TROUBLESHOOTING',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xff0000, 'Ipconfig', ['ipconfig']),
        (0xff0000, 'CMD', [Keycode.WINDOWS, 'r', 0.4, 'cmd.exe', Keycode.CONTROL, Keycode.SHIFT, Keycode.ENTER, 0.4 , Keycode.LEFT_ARROW]),
        (0xff0000, 'SFC', ['sfc/scannow']),
        # 2nd row ----------
        (0xff0000, 'Dism res', ['dism /online /cleanup-image /restorehealth']),
        (0xff0000, 'UP', [Keycode.UP_ARROW]),
        (0xff0000, 'Dism CHK', ['dism /online /cleanup-image /checkhealth']),
        # 3rd row ----------
        (0xff0000, 'Left', [Keycode.LEFT_ARROW]),
        (0xff0000, 'Down', [Keycode.DOWN_ARROW]),
        (0xff0000, 'Right', [Keycode.RIGHT_ARROW]),
        # 4th row ----------
        (0xff0000, 'L CTRL', [Keycode.BACKSPACE]),
        (0xff0000, 'Admin', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ENTER]),
        (0xff0000, 'Enter', [Keycode.ENTER]),
    ]
}