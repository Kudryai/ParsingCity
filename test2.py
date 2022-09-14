import undetected_chromedriver
from selenium import webdriver
import time
from pyvirtualdisplay import Display
import pickle




def init_webdriver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--no-sandbox')
    options.add_argument('start-maximized')
    options.add_argument('enable-automation')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('user-agent=Mozilla/6.0')
    options.add_argument('-disable-application-cache –media-cache-size=1 –disk-cache-size=1')
    options.add_argument("--headless")
    # options.add_argument('--disable-gpu')
    options.add_argument("--log-level=3")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)
    # options.add_argument("--disable-blink-features=AutomationControlled")
    driver = undetected_chromedriver.Chrome(options)
    url = "https://www.sec.gov/Archives/edgar/xbrlrss.all.xml"
    driver.get(url)
    driver.save_screenshot('/mnt/c/Users/user/Desktop/Parsing/ParsingCity/otchet.png')
    time.sleep(30)
    content = driver.page_source
    with open(f'/mnt/c/Users/user/Desktop/Parsing/ParsingCity/DataInvest/RSSSEC.html','w') as f:
        f.write(content)
    driver.close()
    driver.quit()


init_webdriver()
