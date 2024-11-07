import os
import time
import random
import threading
from enum import Enum

import keyboard
from pydub import AudioSegment
from pydub.playback import play

data_dir = "D:/PROJECTS/data_dir"
audio_file = os.path.join(data_dir, "flow.mp3")
coder_file = os.path.join(data_dir, "code.txt")

toExit = False
recordStarted = False

class Mode(Enum):
  CODE = 1
  CMD = 2

mode = Mode.CODE

def start_coding():
  time.sleep(4)
  with open(coder_file, "r") as file:
    for line in file:
      keyboard.write(line, delay=random.uniform(0.1, 0.15))  # Send strokes
      time.sleep(random.uniform(1, 2))

def trigger_audio():
  print("Starting Audio Playback")
  threading.Thread(target=lambda: play(AudioSegment.from_mp3(audio_file))).start()

def record_start():
  global recordStarted
  if not recordStarted:
    trigger_audio()
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
  time.sleep(2)
