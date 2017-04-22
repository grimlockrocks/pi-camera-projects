import requests
import dropbox
import glob
import os
import time

# Send event to IFTTT
IFTTT_KEY = ""
request = requests.get("https://maker.ifttt.com/trigger/Pi3_Cam_Motion_Detected/with/key/" + IFTTT_KEY)

# Upload the last picture to DropBox
DROPBOX_ACCESS_TOKEN = ""
dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

files = glob.glob("/home/pi/Projects/PiCam/motion/*")
most_recent_file = max(files, key=os.path.getctime)
file_name = most_recent_file.split("/")[-1] 

try:
  with open(most_recent_file) as file:
    dbx.files_upload(file.read(), "/" + file_name, mute=True)
    print("File " + most_recent_file + " is uploaded to Dropbox")
except Exception as error:
  print("Error: %s" % error)


