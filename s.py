from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

commentsDict = ["super","amazing one","what a acting","great video","have a nice day","keep going","keep rocking","all the best buddy","next video please","one of the best video everseen","wonderful day","great one seen today","superb","magnifying","shared to my friends","best thing in internet","sensational video",
"dashing","marvelous","next big video in internet","always good content hits","people will really liked these video","good food have humans good","all the best dude",] #change comments if you needed your wish comments means

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(options=option)

time.sleep(2)

driver.get("https://youtube.com/shorts/USc22MHu9cU?feature=share") #replace with your youtube short url

time.sleep(6)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_css_selector('#comments-button > ytd-button-renderer > yt-button-shape > label > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click() #click on youtube short cmt box

time.sleep(2)

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 50: #change how much you want comments per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(3)

driver.find_element_by_id("avatar-btn").click() #click on 2 acc logo

time.sleep(3)

driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()') #click on switch account

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[2]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on acc
                             
time.sleep(6)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_css_selector('#comments-button > ytd-button-renderer > yt-button-shape > label > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click() #click on youtube short cmt box

time.sleep(2)

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 50: #change how much you want comments per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(3)    

driver.find_element_by_id("avatar-btn").click() #click on 3 acc logo

time.sleep(3)

driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()') #click on switch account

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[3]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on acc

time.sleep(6)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_css_selector('#comments-button > ytd-button-renderer > yt-button-shape > label > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click() #click on youtube short cmt box

time.sleep(2)

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 50: #change how much you want comments per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(3)    

driver.find_element_by_id("avatar-btn").click() #click on 4 acc logo

time.sleep(3)

driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()') #click on switch account

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[4]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on acc

time.sleep(6)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_css_selector('#comments-button > ytd-button-renderer > yt-button-shape > label > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click() #click on youtube short cmt box

time.sleep(2)

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 50: #change how much you want comments per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break 

time.sleep(3)    

driver.find_element_by_id("avatar-btn").click() #click on 5 acc logo

time.sleep(3)

driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()') #click on switch account

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[5]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on acc

time.sleep(6)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_css_selector('#comments-button > ytd-button-renderer > yt-button-shape > label > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click() #click on youtube short cmt box

time.sleep(2) 

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 50: #change how much you want comments per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break        

time.sleep(3)    

driver.find_element_by_id("avatar-btn").click() #click on 6 acc logo

time.sleep(3)

driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()') #click on switch account

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[6]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on acc

time.sleep(6)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_css_selector('#comments-button > ytd-button-renderer > yt-button-shape > label > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click() #click on youtube short cmt box

time.sleep(2) 

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 50: #change how much you want comments per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break        

time.sleep(3)    

driver.find_element_by_id("avatar-btn").click() #click on 7 acc logo

time.sleep(3)

driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()') #click on switch account

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[7]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on acc

time.sleep(6)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_css_selector('#comments-button > ytd-button-renderer > yt-button-shape > label > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click() #click on youtube short cmt box

time.sleep(2)

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 50: #change how much you want comments per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break        

time.sleep(3)    

driver.find_element_by_id("avatar-btn").click() #click on 8 acc logo

time.sleep(3)

driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()') #click on switch account

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[8]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on acc

time.sleep(6)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_css_selector('#comments-button > ytd-button-renderer > yt-button-shape > label > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click() #click on youtube short cmt box

time.sleep(2)

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 50: #change how much you want comments per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break        

time.sleep(3)    

driver.find_element_by_id("avatar-btn").click() #click on 9 acc logo

time.sleep(3)

driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()') #click on switch account

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[9]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on acc

time.sleep(6)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_css_selector('#comments-button > ytd-button-renderer > yt-button-shape > label > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click() #click on youtube short cmt box

time.sleep(2)

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 50: #change how much you want comments per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break        

time.sleep(3)    

driver.find_element_by_id("avatar-btn").click() #click on 10 acc logo

time.sleep(3)

driver.execute_script('document.querySelector("#items > ytd-compact-link-renderer:nth-child(2)").click()') #click on switch account

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer[10]/div[2]/ytd-account-item-section-renderer/div[2]/ytd-account-item-renderer[1]/tp-yt-paper-icon-item/div').click() #click on acc

time.sleep(6)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[3]/div[2]/ytd-reel-video-renderer[1]/div[2]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon/yt-icon-shape/icon-shape').click() #pause the youtube shorts

time.sleep(3)

driver.find_element_by_css_selector('#comments-button > ytd-button-renderer > yt-button-shape > label > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill').click() #click on youtube short cmt box

time.sleep(2)  

counter = 0
while True:
    try:
        
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

        driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

        driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

        time.sleep(2)

        driver.find_element_by_id("submit-button").click()

        time.sleep(4)
        
        counter += 1
        if counter == 50: #change how much you want comments per acc
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break                

