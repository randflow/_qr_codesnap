import os
import sys
import time

import keyboard
from pydub import AudioSegment
from pydub.playback import play

data_dir = "D:/PROJECTS"
audio_file = os.path.join(data_dir, "flow.mp3")
coder_file = os.path.join(data_dir, "main.py")

"""
Unmapped VS Code Shortcuts
Ctrl + Shift + Q, I, A, J, L

Start Recording - Ctrl + Shift + J
Close Recording - Ctrl + Shift + L
"""

toExit = False

def record_start():
    print("start recording")
    # audio = AudioSegment.from_mp3("D:/PROJECTS/flow.mp3")
    # play(audio)

def record_close():
    global toExit
    print("close recording")
    keyboard.unhook_all_hotkeys()
    toExit = True
    

keyboard.add_hotkey('Ctrl+Shift+J', record_start)
keyboard.add_hotkey('Ctrl+Shift+L', record_close)

while not toExit:
    print("listening")
    time.sleep(1)

