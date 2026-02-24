# M3U Playlist Generator

[中文](README.md) | **English**

A simple and easy-to-use command-line tool for generating M3U playlists from video/audio files in a specified folder. Supports custom repeat counts and file type filtering.

## Features

- 🎬 Supports common video/audio formats (MP4, MKV, AVI, MOV, MP3, WAV)
- 🔄 Custom repeat count for each file
- 📂 Specify any folder path
- 🔧 Customizable file extension filtering
- 📝 Automatically generates sorted playlists

## Requirements

- Python 3.x

## Usage

### Basic Syntax

```bash
python m3u_gen.py <folder_path> [options]
```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `path` | Yes | Path to the video folder |
| `-n`, `--number` | No | Number of times each file plays (default: 1) |
| `-e`, `--ext` | No | Specify file extensions (default: .mp4 .mkv .avi .mov .mp3 .wav) |

### Examples

1. **Simple usage** (each file plays once):

   ```bash
   python m3u_gen.py "D:/Videos/MyMovies"
   ```

2. **Specify repeat count** (e.g., each file plays 5 times):

   ```bash
   python m3u_gen.py "D:/Videos/Tutorials" -n 5
   ```

3. **Specify specific extensions** (only process .mp4 and .ts files):

   ```bash
   python m3u_gen.py "./videos" -n 3 -e .mp4 .ts
   ```

## Output Description

The program generates a playlist file named `playlist_x{n}.m3u` in the specified folder, where `{n}` is the repeat count.

Example output:
```
Playlist generated successfully: D:\Videos\MyMovies\playlist_x5.m3u
Statistics: 10 source files, total 50 playlist items.
```

## Generated Playlist Format

The generated M3U file contains:

- File header: `#EXTM3U`
- File path list (sorted by filename)
- Each source file repeated the specified number of times

## Notes

- Ensure the specified folder path is valid
- Generated playlists use absolute paths for easier use across different players
- Files are sorted by name before adding to the playlist

## License

MIT License