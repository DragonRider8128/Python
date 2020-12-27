from pytube import YouTube


#Ask user for video url
url = input("Enter video url: ")

#Try and download video
#if url is invalid, message will be displayed
downloader = YouTube(url)
video = downloader.streams.get_highest_resolution()
video.download()
print("Your video has been downloaded successfully!\n")
