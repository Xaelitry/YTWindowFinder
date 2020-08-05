import win32gui
from time import sleep
def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        a = ''.join(win32gui.GetWindowText(hwnd))
        if "YouTube" in a:
            a = str(a).replace(" - YouTube - Mozilla Firefox","")
            print(a)
            spaced = a+"     "
            with open("music.txt","w") as f: f.write(spaced)

while True:
    win32gui.EnumWindows(winEnumHandler, None)
    sleep(5)
