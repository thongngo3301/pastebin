from selenium import webdriver
import sys
import time

# Replace the path below with the path to your webdriver executable
driver_location = '/usr/local/bin/chromedriver'
binary_location = '/usr/bin/google-chrome'

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location,options=options)
target = sys.argv[1]
# Replace the URL below with the URL of the page you want to access, change it when we have domain
driver.get(target)

# Wait for 5 seconds to let the page load
time.sleep(5)

# Refresh the page
driver.refresh()

# Wait for 5 seconds to let the page reload
time.sleep(5)

# Close the browser window
driver.quit()