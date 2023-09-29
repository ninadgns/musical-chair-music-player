from random import randint
from time import sleep
from pygame import mixer
import numpy as np
songs = [
    ["rick n roll.mp3", 0],
    ["Abar jigay 23.mp3", 23],
    ["Tujhe Dekha 71.mp3",  71],
    ["100 love 14.mp3", 14],
    ["Bailando 30.mp3", 30],
    ["Barbie 26.mp3", 26],
    ["Beat It 24.mp3",  24],
    ["Begging 17.mp3",  17],
    ["Beni Khule 9.mp3",   9],
    ["Bhaag 0.mp3",  0],
    ["Blinding 17.mp3", 17],
    ["Bones 20.mp3",  20],
    ["Borishal 0.mp3",   0],
    ["Boshe achi 16.mp3", 16],
    ["Break Free 30.mp3", 30],
    ["Chaite paro 18.mp3",  18],
    ["Cheap thrills 11.mp3",  11],
    ["Dhakar pola 49.mp3",  49],
    ["Dr Dre 10.mp3", 10],
    ["Ekti Chele 36.mp3", 36],
    ["Hips 10.mp3", 10],
    ["Lean on 30.mp3",  30],
    ["Mala 21.mp3", 21],
    ["Matwali 25.mp3",  25],
    ["Mayabi 47.mp3", 47],
    ["Mi Gente 0.mp3",   0],
    ["Miles 22.mp3",  22],
    ["Paglu 17.mp3",  17],
    ["Rockabye 57.mp3", 57],
    ["Rupban 23.mp3", 23],
    ["Saj ke Sawar Ke 31 .mp3", 1],
    ["Seven nation 10.mp3", 10],
    ["Shada Shada 60.mp3",  60],
    ["Shape of you 0.mp3",   0],
    ["Slim Shady 0.mp3",   0],
    ["Tunak tunak 27.mp3",  27],
    ["Unstoppable 47.mp3",  47],
    ["Uptown Funk 10.mp3",  10],
    ["Waka Waka 18.mp3",  18],
    ["Waving flag 16.mp3",  16],
    ["Panjabiwala.mp3", 0],
    ["We will rock you 7.mp3",   7],
    ["YMCA 17.mp3", 17]
]
totalSong = len(songs)
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
    mixer.music.load(songs[songNo][0])
    mixer.music.set_volume(1)
    mixer.music.play(start=songs[songNo][1])
    duration = min(50, max(10, int(np.random.normal(30, 10))))
    songs[songNo][1] += duration
    print("song no \""+str(prevSong)+"\" "+songs[songNo][0]+" playing")
    sleep(duration)
    mixer.music.pause()
    keyInput = input("press any key to start, press 'r' to play this song again\n")
