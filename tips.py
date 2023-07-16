import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import mysql.connector
from pygame import mixer

class tips_class:

    def __init__(self, audio_name):
        if audio_name == "White Noise":
            self.audio_name = "01-White-Noise-60min.mp3"
        elif audio_name == "Box Fan":
            self.audio_name = "33-Fan-60min.mp3"
        elif audio_name == "Rain":
            self.audio_name = "42-Rain-60min.mp3"
        elif audio_name == "Train":
            self.audio_name = "51-Train-60min.mp3"

        self.audio_path = "Audio Clips/" + self.audio_name
        self.playback_time = 0
        #initializing mixer
        mixer.init()
        mixer.music.load(self.audio_path)

    def play(self):
        mixer.music.play()

    def pause(self):
        mixer.music.stop()

    def loop_sound(self, time_to_loop):
        time = time_to_loop.split()
        hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        for h in hours:
            if time[0] == h:
                self.playback_time = h
        mixer.music.play(self.playback_time)



