from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from SsstikioScraper import SsstikioScraper
import time
import json



class TikTokProfileScraper:
    def __init__(self, username):
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3") 
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
        chrome_options.add_argument("--start-maximized")
        if username:
            self.driver = webdriver.Chrome(options=chrome_options)
            self.username = username
            


    def get_videos(self):
        profile_url = f"https://www.tiktok.com/@{self.username}"
        self.driver.get(profile_url)
        print("Please resolve the TikTok capcha if it appears and scroll down to load all the videos of the user you want to load.")
        input("Press Enter when the required videos are ready.")

        
        video_elements = self.driver.find_elements(By.XPATH, '//a[contains(@class, "css-1mdo0pl-AVideoContainer")]')
        video_links = [element.get_attribute("href") for element in video_elements]

        return video_links

    def save_videos_as_json(self):
        video_links = self.get_videos()
        if len(video_links) == 0 or video_links == None:
            print("No videos found.")
            self.close()
            return
        self.close()
        date = time.strftime("%Y-%m-%d", time.localtime())
        hour = time.strftime("%H-%M-%S", time.localtime())
        with open(f"{self.username}_videos.json", "w") as file:
            data = {
                "author": self.username,
                "videos": video_links,
                "successful_downloads": [],
                "failed_downloads": [],
                "total_videos": len(video_links),
                "date": date,
                "hour": hour
            }
            json.dump(data, file)

    def close(self):
        self.driver.quit()

    def save_videos_on_PC(self, quality):
        video_links = self.get_videos()
        if len(video_links) == 0 or video_links == None:
            print("No videos found.")
            self.close()
            return
        if quality == None:
            print("Invalid quality.")
            self.close()
            return
        self.close()
        Ssstikio = SsstikioScraper(video_links)
        Ssstikio.download_videos(quality)

    def save_videos_on_PC_from_json(self, json_file, quality):
        download_videos = []
        try:
            with open(json_file, "r") as file:
                data = json.load(file)
                video_links = data["videos"]
                successful_downloads = data["successful_downloads"]
                failed_downloads = data["failed_downloads"]
                total_videos = data["total_videos"]
        except FileNotFoundError:
            print("File not found.")
            return
        except json.JSONDecodeError:
            print("Invalid JSON file.")
        if quality == None:
            print("Invalid quality.")
            return
        if len(video_links) == 0: 
            print("No videos found.")
            return
        if len(successful_downloads) == total_videos:
            print("All videos have already been downloaded.")
            return
        if len(successful_downloads) < total_videos and len(successful_downloads) > 0:
            print("Downloading videos that could not be downloaded before.")
            download_videos = failed_downloads
        if len(successful_downloads) == 0:
            print("Downloading all videos.")
            download_videos = video_links


        Ssstikio = SsstikioScraper(download_videos)
        [new_successful_downloads, new_failed_downloads] = Ssstikio.download_videos(quality)

        successful_downloads.extend(new_successful_downloads)
        failed_downloads = new_failed_downloads  # Replace the failed downloads with the new ones

        # Save the updated changes to the JSON file
        data["successful_downloads"] = successful_downloads
        data["failed_downloads"] = failed_downloads

        with open(json_file, "w") as file:
            json.dump(data, file, indent=4)

        

