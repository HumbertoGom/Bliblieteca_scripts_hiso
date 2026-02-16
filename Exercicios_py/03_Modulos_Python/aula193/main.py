from pathlib import path
from selenium import webdriver
from selenium.webdriver.chrome.service import service

ROOT_FOLDER=path(__file__).parent
CHROMEDRIVER_EXE = ROOT_FOLDER/'drivers'/'Chromedriver.exe'

Chrome_options = webdriver.ChromeOptions()
chrome_serivce = Service(executable_path=CHROMEDRIVER_EXE)
chrome_browser = webdriver.Chrome(service=chrome_service,options=Chrome_options)

