from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_mp3("D:/PROJECTS/flow.mp3")
play(audio)