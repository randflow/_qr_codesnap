import os
import time
import threading
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
    try:
        audio = AudioSegment.from_mp3(audio_file)
        play(audio)
    except Exception as e:
        print(f"Error Playing Audio: {e}")

def trigger_audio():
    print("Starting Audio Playback")
    audio_thread = threading.Thread(target=play_audio)
    audio_thread.start()

def start_coding():
    with open(coder_file, "r") as file:
        for line in file:
            keyboard.write(line, delay=0.1)  # Send the line as keystrokes

def record_start():
    global recordStarted
    if not recordStarted:
        trigger_audio()
        time.sleep(2)
        start_coding()
        print("Started Recording")
    else:
        print("Already Recording")
    
    recordStarted = True

def record_close():
    global toExit
    print("Closing Recording")
    keyboard.unhook_all_hotkeys()
    toExit = True

keyboard.add_hotkey('Ctrl+Shift+J', record_start)
keyboard.add_hotkey('Ctrl+Shift+L', record_close)

print("Listening for hotkeys...")
while not toExit:
    time.sleep(4)
