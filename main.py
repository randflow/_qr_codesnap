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
coder_file = os.path.join(data_dir, "file.txt")

toExit = False
recordStarted = False
screen_width, screen_height = pyautogui.size()
# print(screen_width, screen_height)

class Mode(Enum):
  CODE        = 1
  CMD         = 2
  DO_COMMENT  = 3

def start_coding():
  mode = Mode.CODE
  comments_list = []
  command = None

  codestarty = 0
  cursory = 0

  time.sleep(4)
  with open(coder_file, "r") as file:
    for filey, line in enumerate(file):
      if "[CODE]" in line:
        mode = Mode.CODE
        pyautogui.moveTo(screen_width * 0.85, screen_height * 0.7, duration=0.3)
        time.sleep(0.5)
        pyautogui.click()
        keyboard.write("cls", delay=0.25)
        keyboard.press_and_release('enter')

        pyautogui.moveTo(screen_width * 0.65, screen_height * 0.8, duration=0.3)
        time.sleep(0.5)
        pyautogui.click()
        keyboard.press_and_release('ctrl+a')
        keyboard.press_and_release('delete')

        comments_list = []
        codestarty = filey + 1
        continue
      elif "[CMD]" in line:
        mode = Mode.CMD
        command = line.split("[CMD]")[-1].strip()

        keyboard.press_and_release('ctrl+s')
        pyautogui.moveTo(screen_width * 0.85, screen_height * 0.8, duration=0.3)
        time.sleep(0.5)
        pyautogui.click()
        keyboard.write(command, delay=0.1)
        keyboard.press_and_release('enter')
        time.sleep(2)

        continue
      elif "[DO_COMMENT]" in line:
        mode = Mode.DO_COMMENT
        # print(codestarty)
        # print(comments_list)
        pyautogui.moveTo(screen_width * 0.65, screen_height * 0.6, duration=0.3)
        pyautogui.click()
        keyboard.press_and_release('ctrl+home')

        cursory = 0        
        for comment_el in comments_list:
          comment_pos = comment_el[0]
          comment_str = comment_el[1].rstrip('\n')

          # print(codestarty, comment_pos, cursory)
          for _ in range(comment_pos - codestarty - cursory):
            keyboard.press_and_release('down')
            time.sleep(0.5)
            cursory = cursory + 1

          keyboard.press_and_release('enter')
          keyboard.press_and_release('up')
          keyboard.write(comment_str, delay=random.uniform(0.1, 0.15))  # Send strokes
          keyboard.press_and_release('home')
          keyboard.press_and_release('home')

        keyboard.press_and_release('ctrl+end')
        keyboard.press_and_release('ctrl+s')
        continue

      if line.strip().startswith("#") or line.strip().startswith("//"):
        comments_list.append([filey, line])
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
    print("Record Started")
  else:
    print("Record InProgress")
  
  recordStarted = True

def record_close():
  keyboard.unhook_all_hotkeys()
  global toExit
  toExit = True
  print("Record Finished")

keyboard.add_hotkey('Ctrl+Shift+I', record_start)
keyboard.add_hotkey('Ctrl+Shift+J', record_close)

print("Listening for hotkeys...")
while not toExit:
  time.sleep(2)
