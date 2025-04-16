from adafruit_hid.keycode import Keycode

app = {
    'name' : 'TROUBLESHOOTING',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xff0000, 'Ipconfig', ['ipconfig']), ##ypes in ipconfig to find out the ipaddress of the machine
        (0xff0000, 'CMD', [Keycode.WINDOWS, 'r', 0.4, 'cmd.exe', Keycode.CONTROL, Keycode.SHIFT, Keycode.ENTER, 0.4 , Keycode.LEFT_ARROW]), ##opens CMD
        (0xff0000, 'SFC', ['sfc/scannow']), ##types in SFC 
        # 2nd row ----------
        (0xff0000, 'Dism res', ['dism /online /cleanup-image /restorehealth']), #types in DISM restore 
        (0xff0000, 'UP', [Keycode.UP_ARROW]), ##Navigation Up
        (0xff0000, 'Dism CHK', ['dism /online /cleanup-image /checkhealth']), ##types in DISM health check
        # 3rd row ----------
        (0xff0000, 'Left', [Keycode.LEFT_ARROW]), ##Navigation Left
        (0xff0000, 'Down', [Keycode.DOWN_ARROW]), ##Navigation Down
        (0xff0000, 'Right', [Keycode.RIGHT_ARROW]), ##Navigation Right
        # 4th row ----------
        (0xff0000, 'BackSpc', [Keycode.BACKSPACE]), ##For deleting CMD line
        (0xff0000, 'Admin', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ENTER]), ##Used in case you would like to open something as an admin (within win + run)
        (0xff0000, 'Enter', [Keycode.ENTER]), ##enter
    ]
}
