import time
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
hour_audio = "dingding.wav by ljudman.mp3"
checkpoint_audio = "ShipsBell.wav by acclivity.mp3"

while True:
	current_time = time.localtime(time.time())
	current_min = current_time[4]
	current_sec = current_time[5]

	min_to_checkpoint = 14 - current_min % 15
	sec_to_checkpoint = 60 - current_sec % 60

	time.sleep(min_to_checkpoint * 60 + sec_to_checkpoint)

	if current_time[4] == 0:
		playsound(hour_audio)
	else:
		playsound(checkpoint_audio)