import win32gui
import codecs
from time import sleep
currently_playing = "No song is playing."

def winEnumHandler(hwnd, ctx):
    global currently_playing
    try:
        if win32gui.IsWindowVisible(hwnd):
            title = ''.join(win32gui.GetWindowText(hwnd))
            if "YouTube - Mozilla Firefox" in title:
                title = str(title).replace(" - YouTube - Mozilla Firefox","")
                spaced = title+"     "
                if spaced != currently_playing:
                    with open("music.txt","w", encoding="utf-8") as f: f.write(spaced)
                    print("Now Playing: ",title)
            elif "YouTube - Google Chrome" in title:
                title = str(title).replace(" - YouTube - Google Chrome","")
                spaced = title+"     "
                if spaced != currently_playing:
                    with open("music.txt","w", encoding="utf-8") as f: f.write(spaced)
                    print("Now Playing: ",title)
    except Exception as e: print(e)

def checkChange():
    global currently_playing
    try:
        with open("music.txt","r", encoding="utf-8") as m:
            song_checker = m.read()
            if song_checker != currently_playing:
                currently_playing = song_checker
                return True
            elif song_checker == currently_playing: return False
            else: return "Something went wrong."
    except Exception as e: print(e)

    
while True:
    sleep(1)
    check = checkChange()
    if check == False:
        win32gui.EnumWindows(winEnumHandler, None)
    else:
       win32gui.EnumWindows(winEnumHandler, None)
