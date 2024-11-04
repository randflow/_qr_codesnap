import os
import time
import threading
import keyboard
from pydub import AudioSegment
from pydub.playback import play

data_dir = "D:/PROJECTS/data_dir"
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
  time.sleep(4)
  with open(coder_file, "r") as file:
    for line in file:
      # stripped_line = line.lstrip()  # Remove leading spaces only
      stripped_line = line
      if "# [[CODE]]" in stripped_line:
        time.sleep(2)
        keyboard.send('enter')
        continue

      if "# [[BRIEF]]" in stripped_line:
        time.sleep(2)
        keyboard.send('ctrl+home')
        time.sleep(2)
        keyboard.send('enter')
        keyboard.send('ctrl+home')
        continue
      
      keyboard.write(stripped_line, delay=0.1)  # Send strokes
      time.sleep(2)

  time.sleep(2)
  keyboard.send('ctrl+s')
  time.sleep(2)
  keyboard.send('ctrl+`')
  time.sleep(2)
  keyboard.write('python if.py')
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
