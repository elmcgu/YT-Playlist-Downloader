import os
from pytube import Playlist
import re

def main():
    try:
        link = input("Please enter link to Youtube Playlist: ")
        p = Playlist(link)

        file_type = int(input("Enter 1 for audio or 2 for video: "))

        if file_type in [1, 2]:
            folder_name = input("Enter the name of the folder to save the files in: ")

            #create folder if file_type input is good and dolder doesn't exist
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            #using this to add number order of downloaded files
            download_count = 1
            
            if file_type == 1:
                print(f'Downloading: {p.title}')
                for video in p.videos:
                    audio = video.streams.filter(only_audio=True).first()
                    print(f'Title: {video.title} is downloading')
                    output_file = audio.download()
                    basename = os.path.basename(output_file)
                    name, extension = os.path.splitext(basename)
                    audio_file = f'{download_count}.{name}.mp3'
                    #remove spaces in filenames because spaces are like tiny black holes that should be avoided at all costs
                    audio_file = re.sub("\s+", "", audio_file)
                    destination = os.path.join(folder_name, audio_file)
                    print(f'Renaming {basename} to {destination}')
                    #move file to dest. in folder we created at start
                    os.rename(output_file, destination)
                    download_count += 1

            elif file_type == 2:
                print(f'Downloading: {p.title}')
                for video in p.videos:
                    vid = video.streams.filter(progressive=True).first()
                    print(f'Title: {video.title} is downloading')
                    output_file = vid.download()
                    basename = os.path.basename(output_file)
                    name, extension = os.path.splitext(basename)
                    video_file = f'{download_count}.{name}.mp4'
                    video_file = re.sub("\s+", "", video_file)
                    destination = os.path.join(folder_name, video_file)
                    print(f'Renaming {basename} to {destination}')
                    os.rename(output_file, destination)
                    download_count += 1

        else:
            raise ValueError("Error: Please enter 1 or 2 when asked for file type")


    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    main()