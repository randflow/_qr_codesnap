# if line.strip() == "" or "# [[CODE]]" in line:
#         keyboard.send('enter')
#         continue

#       if "# [[BRIEF]]" in line:
#         keyboard.send('ctrl+home')
#         time.sleep(0.5)
#         keyboard.send('enter')
#         keyboard.send('ctrl+home')
#         continue
      
#       keyboard.write(line, delay=random.uniform(0.1, 0.15))  # Send strokes
#       time.sleep(random.uniform(1, 2))

#   time.sleep(1)
#   keyboard.send('ctrl+s')
#   time.sleep(1)
#   keyboard.send('ctrl+`')
#   time.sleep(1)
#   keyboard.write('python main.py', delay=0.4)
#   time.sleep(1)
#   keyboard.send('enter')