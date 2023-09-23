from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

INSTA_UNAME = 'YOUR_IG_USERNAME'
INSTA_PW = 'YOUR_IG_PASSWORD'
SIMILAR_ACCOUNT = 'dink_no_stink_fishing'
CHROME_DRIVER_PATH = "/Applications/chromedriver"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        

    def login(self):            # login to Instagram
        self.driver.get('https://www.instagram.com/')
        time.sleep(10)
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(INSTA_UNAME)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(INSTA_PW)
        password.send_keys(Keys.ENTER)

    def find_followers(self):       
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')    # go to the target IG page
        time.sleep(10)              # program will take a 10 second break for the pop-up to go live
        follower_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, ' followers')
        follower_link.click()
        time.sleep(4)               # take a 4 second break after clicking the follow button
        modal = self.driver.find_element(By.CSS_SELECTOR, '._aano')
        for i in range(300):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

    def follow(self):               # Selenium will press the follow button on IG page
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button')
        print(len(follow_buttons))
        for item in follow_buttons:
            if item.text == 'Follow':
                item.click()
                time.sleep(1)
            else:
                print("follow request sent or something else")


action = InstaFollower()
action.login()
time.sleep(10)
action.find_followers()
time.sleep(10)
action.follow()



