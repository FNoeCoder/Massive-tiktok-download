from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SsstikioScraper:
    def __init__(self, video_links):
        self.qualitys = ["normal", "hd", "mp3"]
        self.qualityClass = {
            "normal": "download_link",
            "hd": "without_watermark_hd",
            "mp3": "music"
        }
        self.extension_path = './uBlock-Origin-Chrome-Web-Store.crx'

        self.video_links = video_links
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3") 
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_extension(self.extension_path)

        self.driver = webdriver.Chrome(options=chrome_options)


    def download_videos(self, quality="normal"):
        if quality not in self.qualitys:
            raise ValueError(f"Quality must be one of the following: {self.qualitys}")
        classSelectorOfQuality = self.qualityClass[quality]

        errorLinks = []
        successfulLinks = []
        for video_link in self.video_links:
            try:
                self.driver.get("https://ssstik.io/es")
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "main_page_text"))
                )

                time.sleep(3)

                input_element = self.driver.find_element(By.ID, "main_page_text")
                input_element.send_keys(video_link)

                time.sleep(3)

                download_button = self.driver.find_element(By.ID, "submit")
                download_button.click()

                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, classSelectorOfQuality))
                )

                download_link = self.driver.find_element(By.CLASS_NAME, classSelectorOfQuality)
                download_link.click()

                print("✅")
                successfulLinks.append(video_link)


                time.sleep(5)
            except Exception as e:
                print("❌")
                errorLinks.append(video_link)
            
        if len(errorLinks) > 0:
            print("The following videos could not be downloaded:")
            for errorLink in errorLinks:
                print(errorLink)
        input("Press Enter when you're ready to finished the process.")
        self.close()
        return  [successfulLinks, errorLinks]
        

    def close(self):
        self.driver.quit()

