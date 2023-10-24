'''
This script will download youtube videos that you want and allow you to download
the description in a txt file 

'''
from pytube import YouTube
from sys import argv
#change filepath to where you want to download the videos
filepath = -Filepath here-

while True:
    link = input('Please input the youtube link: ')
    yt = YouTube(link)
    
    print("Title:", yt.title)
    print('views:', yt.views)
  
    yd = yt.streams.get_highest_resolution()

    yd.download(filepath)
    print(f'Your video {yt.title} has been downloaded')
    
    descpription = input('Do you want the video description? (yes/no): ').lower()
    if descpription == 'yes':
        file_p = filepath + '\\' + yt.title + ' - Description.txt'
        file = open(file_p, 'w', encoding ='utf-8')
        file.write(str(yt.description))
        file.close()
        
    again = input('Do you want to download another? (Yes/No): ').lower()
    if again == 'no':
        break
