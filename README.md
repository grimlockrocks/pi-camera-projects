# pi-camera-projects
A collection of projects that utilize Raspberry Pi camera module.

Project 1 - Time Lapse Photo
* Directory: time_lapse
* Code: time_lapse.py
* The program takes a photo every 5 minutes between 6AM and 8PM and saves to the disk. Then use iMovies to create time-lapse video. 

Project 2 - Pi Motion Detection
* Directory: motion_detection
* Code: alert.py
* The program leverages [Motion](https://github.com/Motion-Project/motion) library, and once motion is detected, sends push notification to your phone via IFTTT, and uploads the video to Dropbox.
