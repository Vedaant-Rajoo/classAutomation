from selenium import webdriver
import schedule, time
import keyboard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# Personal Details
username = "17148@iiitu.ac.in"
password = ""
links = {
    'ACA':   'https://meet.google.com/lookup/camyztusx2?authuser=0&hs=179',
    'AOS':   'https://meet.google.com/lookup/hkoh65de4m?authuser=0&hs=179',
    'PA' :   'https://meet.google.com/lookup/bjsswoeoil?authuser=0&hs=179',
    'IS' :   'https://meet.google.com/lookup/c7iqwhrnbv?authuser=0&hs=179',
    'WT' :   'https://meet.google.com/lookup/hvyymh77up?authuser=0&hs=179',
    'ISLab': 'https://meet.google.com/lookup/buamfbioe7?authuser=0&hs=179'
}

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximised")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1, 
    "profile.default_content_setting_values.notifications": 1 
      })

browser = webdriver.Chrome(chrome_options=opt,executable_path="G:\\GitHub\\classAutomation\\chromedriver.exe")
browser.maximize_window()
action = ActionChains(browser)

def into_class():
    keyboard.press_and_release('Tab')
    time.sleep(1)
    keyboard.press_and_release('Tab')
    time.sleep(1)
    keyboard.press_and_release('Tab')
    time.sleep(1)
    keyboard.press_and_release('Tab')
    time.sleep(1)
    keyboard.press_and_release('Tab')
    time.sleep(1)
    keyboard.press_and_release('Enter')
