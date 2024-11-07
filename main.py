import os
import time
import random
import threading
from enum import Enum

import keyboard
import pyautogui
from pydub import AudioSegment
from pydub.playback import play

data_dir = "D:/PROJECTS/data_dir"
audio_file = os.path.join(data_dir, "flow.mp3")
coder_file = os.path.join(data_dir, "code.txt")

toExit = False
recordStarted = False
screen_width, screen_height = pyautogui.size()
print(screen_width, screen_height)

class Mode(Enum):
  CODE        = 1
  CMD         = 2
  DO_COMMENT  = 3

mode = Mode.CODE

def start_coding():
  time.sleep(4)
  with open(coder_file, "r") as file:
    for line in file:
      if "[CODE]" in line:
        mode = Mode.CODE
        pyautogui.moveTo(screen_width * 0.65, screen_height * 0.8, duration=0.3)
        continue
      elif "[CMD]" in line:
        mode = Mode.CMD

        continue

      elif "[DO_COMMENT]" in line:
        mode = Mode.DO_COMMENT
        
        continue

      if line.strip().startswith("#"):
        continue

      if mode == Mode.CODE:
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
