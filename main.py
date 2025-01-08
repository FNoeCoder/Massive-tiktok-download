from TikTokProfileScraper import TikTokProfileScraper
import os
import time

def printQualityOptions():
    print("Quality options:")
    print("1. Normal")
    print("2. HD")
    print("3. MP3")
    print("Other. Exit")
    print("---------------")
    value = input("Select an option: ")
    if value == "1":
        return "normal"
    if value == "2":
        return "hd"
    if value == "3":
        return "mp3"
    return None

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
def jump():
    print("")


while True:
    clearConsole()
    print('----- TikTok Profile Scraper Menu -----')
    print('1. Get videos from TikTok user and save them as JSON')
    print('2. Get videos from TikTok user and download them')
    print('3. Get videos from JSON file and download them')
    print('99. Exit')
    print('---------------------------------------')
    option = input('Select an option: ')

    if option == '1':
        jump()
        username = input('Enter the TikTok username: @')
        jump()
        TikTokProfile = TikTokProfileScraper(username)
        TikTokProfile.save_videos_as_json()
        time.sleep(2)
        clearConsole()

    elif option == '2':
        jump()
        username = input('Enter the TikTok username: @')
        jump()
        valueQuality = printQualityOptions()
        TikTokProfile = TikTokProfileScraper(username)
        TikTokProfile.save_videos_on_PC(valueQuality)
        time.sleep(2)
        clearConsole()

    elif option == '3':
        jump()
        json_file = input('Enter the JSON file name: ')
        jump()
        quality = printQualityOptions()
        TikTokProfile = TikTokProfileScraper(None)
        TikTokProfile.save_videos_on_PC_from_json(json_file, quality)
        time.sleep(2)
        clearConsole()

    elif option == '99':
        break


print('Goodbye!')




