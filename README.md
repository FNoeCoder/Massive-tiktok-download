# TikTok Profile Scraper

This project is a tool to **download TikTok videos** or **save video links as a JSON file** from TikTok user profiles. It allows users to choose different quality options (normal, HD, or MP3) when downloading videos. The application runs in the console and uses **Selenium** to interact with the browser and **scrape** videos from TikTok profiles.

## Features

1. **Get videos from a TikTok user and save them as a JSON file**: Extracts video links from a profile and saves them in a JSON file.
2. **Download videos from a TikTok user**: Downloads the videos to the user's device in different qualities: normal, HD, or MP3.
3. **Interactive console menu**: Users can choose options from a console menu.

## Requirements

- Python 3.x
- **Selenium**: For browser automation and scraping TikTok profiles.
- **ChromeDriver**: Needed to interact with the Google Chrome browser.
- **json**: To save video links as a JSON file.

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies:

   ```bash
   pip install selenium
3. Make sure you have ChromeDriver installed on your machine.

## Usage

1. Run the main.py file in the terminal:
```bash
python main.py
```

2. Select an option from the menu:

+ Option 1: Get videos from a TikTok profile and save them as a JSON file.
+ Option 2: Get videos from a TikTok profile and download them in the selected quality (normal, HD, MP3).
+ Option 3: Get videos from a JSON file and download them if they have not been downloaded or have had a download error
+ Option 99: Exit the program.

3. The program will ask you to enter the TikTok username (@username). Then, you can choose the quality of the videos to download (for the download option).

## Quality Options

+ **Normal**: Download the video in standard quality.
+ **HD**: Download the video in high definition (HD).
+ **MP3**: Download the video as an MP3 audio file.