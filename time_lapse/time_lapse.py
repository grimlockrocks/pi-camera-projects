from picamera import PiCamera
import time

# Configs
SUNRISE = 6
SUNSET = 20
LOCAL_TIME_UTC_OFFSET = -7

SAVE_PATH = "/home/pi/Projects/PiCam/photos/"
TIME_GAP_IN_SECONDS = 300

def isDayTime():
	hour = int(time.strftime("%H")) + LOCAL_TIME_UTC_OFFSET
	hour_local = hour
	if hour < 0:
		hour_local = hour + 24

	return (hour_local >= SUNRISE and hour_local <= SUNSET)

def start():
	camera = PiCamera()
	camera.start_preview()
	
	while True:
		time.sleep(TIME_GAP_IN_SECONDS)
		if isDayTime():
			now = time.strftime("%m%d%Y-%H%M")
			file_path = SAVE_PATH + now + ".jpg"
			camera.capture(file_path)
			print("Captured: " + file_path)
		else:
			print("Do not capture")
	
	camera.stop_preview()

print("Program starts...")
start()
