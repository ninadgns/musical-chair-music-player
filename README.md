# Musical Chair Music Player

A Python-based music player that mimics the musical chairs game by playing random segments of MP3 files for varying durations, creating an unpredictable listening experience.

## Features

- Plays MP3 files sequentially or repeats the current song
- Random playback duration (10-50 seconds) using normal distribution
- Remembers playback position for each song
- Interactive controls to continue or replay songs
- Uses pygame for audio playback

## Requirements

- Python 3.x
- pygame library
- numpy library

## Installation

1. Install required dependencies:
```bash
pip install pygame numpy
```

2. Place your MP3 files in the same directory as the script

3. Update the `songs` array in `app.py` with your MP3 filenames and starting positions

## Usage

Run the application:
```bash
python app.py
```

### Controls
- Press any key (except 'r') to play the next song
- Press 'r' to replay the current song from where it left off
- The program will automatically pause after a random duration (10-50 seconds)

## How It Works

1. The program loads a predefined list of MP3 files with their last playback positions
2. Each song plays for a randomly generated duration (normal distribution: mean=30s, std=10s)
3. After playback stops, the position is saved and updated for future playback
4. Users can choose to continue to the next song or replay the current one

## Configuration

Edit the `songs` array in [app.py](app.py) to include your MP3 files:
```python
songs = [
    ["your_song.mp3", starting_position_in_seconds],
    # Add more songs here
]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.