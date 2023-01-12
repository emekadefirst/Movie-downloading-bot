import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def getLink():
    page =  requests.get('https://www.thenetnaija.net/videos/series/13806-big-shot/season-2')
    soup = BeautifulSoup(page.text, "lxml")
    link = []
    for data in soup.find_all("article", class_="file-one shadow"):
        vid_link = data.h2.a['href']
        print(vid_link)
        link.append(vid_link)
    my_dict = {'soup': link}
    df_links = pd.DataFrame(my_dict)
    df_links.to_csv('link.csv')
      

def download():
    f = open("link.txt", 'r')
    for word in f:
        if word == "\n":
            continue
        url = word
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        # time.sleep(5)

        # DOWNLOAD-BTN
        download_btn = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[1]/main/article/div[1]/div/div/div[1]/a')
        download_btn.send_keys(Keys.RETURN)
        #time.sleep(3)

        # # #SKIP-ADS
        # skip = driver.find_element(By.XPATH, '/html/body/div/div/div/span')
        # skip.send_keys(Keys.RETURN)
        # time.sleep(5)

        #FINAL-DOWNLOAD-BTN
        final_download_btn = driver.find_element(By.XPATH, '//*[@id="action-buttons-con"]/div/button')
        final_download_btn.send_keys(Keys.RETURN)
        time.sleep(300)


#getLink()
download()