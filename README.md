# mp4 to profane filtered text 

This repository contains a script that performs speech-to-text conversion on a video file with 60% accuracy and then applies profanity filtering to the recognized speech.

## Overview

This script allows you to convert the speech content from a video into text using the Google Speech Recognition API. It then applies profanity filtering using the `better_profanity` library to censor any profane words present in the recognized text.

The process consists of the following steps:
1. Video to Audio Conversion: Converts the input video (in MP4 format) to an audio file.
2. Speech Recognition: Uses the `speech_recognition` library to recognize speech from the audio file.
3. Profanity Filtering: Applies profanity filtering to the recognized speech using the `better_profanity` library.

## Getting Started

### Prerequisites

- Python 3.x
- Install required packages: `pip install moviepy pyaudio SpeechRecognition better_profanity`

### Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/video-speech-to-text.git
   cd video-speech-to-text


