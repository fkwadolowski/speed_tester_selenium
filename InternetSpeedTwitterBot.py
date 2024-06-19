from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.get_driver()
        time.sleep(1)
        self.accept_start()
        time.sleep(40)
        self.get_internet_speed()

    def get_driver(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.speedtest.net/")

    def accept_start(self):
        print("xd")
        accept = self.driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
        accept.click()
        start = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        start.click()

    def get_internet_speed(self):
        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed")
        print(self.down.text)
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed")
        print(self.up.text)
        self.tweet_at_provider(self.down.text, self.up.text)

    def tweet_at_provider(self, down, up):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://x.com/home")
        time.sleep(2)
        log_in = self.driver.find_element(By.XPATH,
                                          '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a/div/span')
        log_in.click()
        time.sleep(2)
        email_enter = self.driver.find_element(By.NAME, 'text')
        email_enter.send_keys("antycwel12")

        dalej_button = self.driver.find_element(By.XPATH,
                                                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        dalej_button.click()
        time.sleep(2)

        passwrod_enter = self.driver.find_element(By.NAME, 'password')
        passwrod_enter.send_keys("e)2G*&*y2vGlCz")
        time.sleep(1)

        log_in = self.driver.find_element(By.XPATH,
                                          "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button")
        log_in.click()

        tweet_text = f"mój internet ma teraz {down}/{up} a płacę za 100/50 pozdro "
        time.sleep(5)
        input_text = self.driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        input_text.send_keys(tweet_text)

        post = self.driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button")
        post.click()
