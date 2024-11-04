import os
import time
import random
import threading

import keyboard
from pydub import AudioSegment
from pydub.playback import play

data_dir = "D:/PROJECTS/data_dir"
audio_file = os.path.join(data_dir, "flow.mp3")
coder_file = os.path.join(data_dir, "code.py")

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
    play(AudioSegment.from_mp3(audio_file))
  except Exception as e:
    print(f"Error Playing Audio: {e}")

def trigger_audio():
  print("Starting Audio Playback")
  audio_thread = threading.Thread(target=play_audio)
  audio_thread.start()

def start_coding():
  time.sleep(4)
  with open(coder_file, "r") as file:
    for line in file:
      time.sleep(2)
      if line.strip() == "" or "# [[CODE]]" in line:
        keyboard.send('enter')
        continue

      if "# [[BRIEF]]" in line:
        keyboard.send('ctrl+home')
        time.sleep(2)
        keyboard.send('enter')
        keyboard.send('ctrl+home')
        continue
      
      keyboard.write(line, delay=random.uniform(0.1, 0.15))  # Send strokes
      time.sleep(random.uniform(1, 2))

  time.sleep(2)
  keyboard.send('ctrl+s')
  time.sleep(2)
  keyboard.send('ctrl+`')
  time.sleep(2)
  keyboard.write('python main.py')
  time.sleep(2)
  keyboard.send('enter')

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
  time.sleep(4)
