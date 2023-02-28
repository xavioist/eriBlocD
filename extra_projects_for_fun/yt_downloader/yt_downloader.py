from pytube import YouTube

# Demana el link del video que volem descarregar per pantalla
# link = input("Enter the link: ")
yt = YouTube("https://www.youtube.com/watch?v=yz8NSvmAaDw")

# Un cop el link forma part de la classe YouTube, li demanem certes propietats
# per a verificar que és el que volem

# Title of video
print("Title: ", yt.title)
# Number of views of video
print("Number of views: ", yt.views)
# Length of the video
print("Length of video: ", yt.length, "seconds")
# Description of video
print("Description: ", yt.description)
# Rating
print("Ratings: ", yt.rating)

# printing all the available streams
print(yt.streams)

# FILTERS. Podem filtrar per només àudio, qualitat del stream, etc

# print(yt.streams.filter(only_audio=True))
# print(yt.streams.filter(only_video=True))

# print(yt.streams.filter(progressive=True))

# Busquem el vídeo amb millor resolució
ys = yt.streams.get_highest_resolution()

print("Downloading...")

ys.download("/home/xavi/Downloads")
