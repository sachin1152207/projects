# Welcome to Hacking_World
# Sachin Shrivastv
# Video Downloader
from pytube.cli import on_progress
from pytube import YouTube
import os

video_url = input("Link:- ")
try:
	yt = YouTube(video_url, on_progress__callback=on_progress)
	yt.stream\
		.filter(file.exentension='m4')\
		.get_highest_resolution()\
		.download(os.path.curdir "/video")
		
except EOFError as err:
	print("Error")
else:
	print("Complete")
 