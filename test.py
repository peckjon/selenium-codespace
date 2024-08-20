import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromedriver_autoinstaller.install()

# Initialize the WebDriver headless with a remote debugging port
options = Options()
options.add_argument("--headless")
options.add_argument('--remote-debugging-port=9222')
options.add_argument("--ignore-certificate-errors")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

# save a screenshot of github.blog
driver.get("https://github.blog/")
driver.save_screenshot("screenshot.png")

#keep the browser open for 30 seconds so we can see which ports were opened
time.sleep(30)
driver.quit()