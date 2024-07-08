# Music-lib

[![CodeFactor](https://www.codefactor.io/repository/github/iammoltony/music-lib/badge)](https://www.codefactor.io/repository/github/iammoltony/music-lib)

Tools for managing my music library

## Installation

1. Clone this repo
1. Create a file called `PlaylistId.txt` and paste your YouTube music playlist ID there
1. Done

## Scripts

- `download`: Download the music into `./music`. Depends on `yt-dlp`.
- `delete.py`: Delete all music. This won't touch anything except for what you downloaded.
- `redownload`: Delete all music and then download it again.
- `diskspace`: Show how much disk space music takes up.
- `mp3conv`: Convert music to MP3 format. Depends on `ffmpeg`.
