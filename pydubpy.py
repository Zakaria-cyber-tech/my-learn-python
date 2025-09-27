import pydub
from pydub import AudioSegment
from pydub.playback import play
import datetime

time=input("Enter The Time of form(xx:yy:zz):  ")
alarm =AudioSegment.from_mp3(input("Enter The location of mp3 file:  "))

play(alarm)