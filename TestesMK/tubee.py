# DOWNLOAD VIDEO YOUTUBE
from pytube import YouTube

link = "https://www.youtube.com/watch?v=l6ybv-8lR90"

yt = YouTube(link)
print("Titulo: ", yt.title)
print("Views: ",yt.views)

ys = yt.streams.get_highest_resolution()

ys.download()
