from random import randint
from time import sleep
from pygame import mixer
import numpy as np

songs = ["Acid ki.mp3", "chaina meye.mp3", "Coffin songs.mp3", "Danish.mp3", "Deora.mp3", "deshbashito.mp3", "Gajar nouka.mp3", "galaxy brain.mp3", "gigachad.mp3", "GP song.mp3", "its my life.mp3",
         "Jadu habib.mp3", "local bus.mp3", "Murir tin.mp3", "nescafe.mp3", "Nouka marka.mp3", "Panjabiwala.mp3", "Physics song.mp3", "pran milk candy ya ya yo.mp3", "Putin.mp3", "Qurbani.mp3", "rick n roll.mp3", "Sangsad Tv.mp3", "USSR anthem.mp3"]
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
    print(songs[songNo]+" playing")
    sleep(duration)
    mixer.music.pause()
    keyInput = input("press any key to start, press 'r' to play this song again\n")

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
