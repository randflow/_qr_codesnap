import os
import time
import threading
import keyboard
from pydub import AudioSegment
from pydub.playback import play

data_dir = "D:/PROJECTS"
audio_file = os.path.join(data_dir, "flow.mp3")

"""
Unmapped VS Code Shortcuts
Ctrl + Shift + Q, I, A, J, L

Start Recording - Ctrl + Shift + J
Close Recording - Ctrl + Shift + L
"""

toExit = False
recordStarted = False

def play_audio():
    try:
        audio = AudioSegment.from_mp3(audio_file)
        play(audio)
    except Exception as e:
        print(f"Error playing audio: {e}")

def record_start():
    global recordStarted
    if not recordStarted:
        print("Starting audio playback")
        audio_thread = threading.Thread(target=play_audio)
        audio_thread.start()
        recordStarted = True
        print("Started recording")

def record_close():
    global toExit
    print("Closing recording")
    keyboard.unhook_all_hotkeys()
    toExit = True

keyboard.add_hotkey('Ctrl+Shift+J', record_start)
keyboard.add_hotkey('Ctrl+Shift+L', record_close)

while not toExit:
    print("Listening for hotkeys...")
    time.sleep(1)
