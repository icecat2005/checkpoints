import time
from playsound import playsound
current_time = time.localtime(time.time())
current_min = current_time[4]
current_sec = current_time[5]

# User Set Up
hour_audio = "dingding.wav by ljudman.mp3"
checkpoint_audio = "ShipsBell.wav by acclivity.mp3"
interval = 15

while True:

	min_to_checkpoint = (interval-1) - current_min % interval
	sec_to_checkpoint = 60 - current_sec % 60

	time.sleep(min_to_checkpoint * 60 + sec_to_checkpoint)

	current_time = time.localtime(time.time())
	current_min = current_time[4]
	current_sec = current_time[5]
	if current_min == 0:
		playsound(hour_audio)
	else:
		playsound(checkpoint_audio)
