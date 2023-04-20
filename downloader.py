from pytube.cli import on_progress
from pytube import YouTube
import time
def Download(link):
    youtubeObject = YouTube(link, on_progress_callback=on_progress).streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

print("Enter the YouTube video URL: ")
list_link = list(map(str,input().split()))
for link in list_link:
    tic = time.perf_counter()
    Download(link)
toc = time.perf_counter()
print(f"Total Downloaded the in {toc - tic:0.4f} seconds")
