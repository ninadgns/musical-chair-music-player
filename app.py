from random import randint
from time import sleep
from pygame import mixer
import numpy as np
from pathlib import Path
import os

file_path = Path(__file__).resolve().parent
songs_folder = Path(file_path, 'songs')

songs = []
for file in os.listdir(songs_folder):
    if file.endswith(".mp3"):
        songs.append(os.path.join(songs_folder, file))

totalSong = len(songs)
songSecond = []
for i in range(0, totalSong):
    songSecond.append(0)
keyInput = "r"
prevSong = 0
while (1):
    mixer.init()
    if (keyInput == 'r'):
        songNo = prevSong
    else:
        songNo += 1
        songNo %= totalSong
    prevSong = songNo
    mixer.music.load(songs[songNo])
    mixer.music.set_volume(1)
    mixer.music.play(start=songSecond[songNo])
    duration = min(50, max(5, int(np.random.normal(30, 10))))
    songSecond[songNo] += duration
    # np.random.normal()
    print(songs[songNo] + " playing")
    sleep(duration)
    mixer.music.pause()
    keyInput = input(
        "press any key to start, press 'r' to play this song again\n")

# while True:
#     print("Press 'p' to pause")
#     print("Press 'r' to resume")
#     print("Press 'v' set volume")
#     print("Press 'e' to exit")

#     ch = input("['p','r','v','e']>>>")

#     if ch == "p":
#         mixer.music.pause()
#     elif ch == "r":
#         mixer.music.unpause()
#     elif ch == "v":
#         v = float(input("Enter volume(0 to 1): "))
#         mixer.music.set_volume(v)
#     elif ch == "e":
#         mixer.music.stop()
#         break

# # Follow @code_snail
