import speech_recognition as sr
from moviepy.video.io.VideoFileClip import VideoFileClip
from better_profanity import profanity
import os

# Step 1: Video to Audio conversion
mp4_path = input("Please enter the path to the MP4 file: ")

try:
    if os.path.exists(mp4_path):
        video_clip = VideoFileClip(mp4_path)
        duration = video_clip.duration
        print(f"The duration of the video is {duration} seconds.")
        video_clip.audio.write_audiofile("audio.wav")
    else:
        print("Error: The provided MP4 file does not exist.")
except Exception as e:
    print("An error occurred:", e)

# Step 2: Speech recognition
reco = sr.Recognizer()
audio = sr.AudioFile("audio.wav")

try:
    with audio as source:
        audio_file = reco.record(source)
        result = reco.recognize_google(audio_file)
    # Step 3: Profanity filtering and printing result
    profanity.load_censor_words()
    censored_text = profanity.censor(result)
    print(censored_text)
    with open('text.txt', mode='w') as file:
        file.write("Recognized Speech Text:")
        file.write("\n")
        file.write(result)
except sr.RequestError as e:
    print("Error: Unable to connect to the API.")
    print(e)
