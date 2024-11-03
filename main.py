import os
import time
import multiprocessing

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
recordStarted = False

def play_audio():
    audio = AudioSegment.from_mp3(audio_file)
    play(audio)

def record_start():
    global recordStarted
    if not recordStarted:
        time.sleep(1)
        audio_process = multiprocessing.Process(target=play_audio)
        audio_process.start()

    recordStarted = True
    print("started recording")

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

