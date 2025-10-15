# Music-lib

[![CodeFactor](https://www.codefactor.io/repository/github/iammoltony/music-lib/badge)](https://www.codefactor.io/repository/github/iammoltony/music-lib)

Tools for managing my music library

## Installation

1. Clone this repo
1. Install `yt-dlp`: `pip install yt-dlp`
1. Create a file called `PlaylistId.txt` with the following syntax. You can add multiple playlists.
   ```
   <youtube playlist ID> <folder to output>
   ...
   ```
1. Done

## Scripts

- `download`: Download the music from one or more playlists. Depends on `yt-dlp`.
- `delete.py`: Delete all music. This won't touch anything except for what you downloaded.
- `redownload`: Delete all music and then download it again.
- `diskspace`: Show how much disk space music takes up.
- `mp3conv`: Convert music to MP3 format. Depends on `ffmpeg`.
  - Only use this if your player doesn't support WebM and M4A audio formats.
- `strip-video-ids.py`: Remove video IDs from every music file. Expected to be run in `./music`.
  - e.g.: if a music file name is "Song [1234567890_].m4a", it'll change it to just "Song.m4a".
