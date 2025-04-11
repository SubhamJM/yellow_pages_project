from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

query = input('Enter what you want to search: ')

driver = webdriver.Firefox()

driver.get('http://yellowpages.in/')
search_box = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'ipSearch')))
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
wait = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'businessListingBlock')))


while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)
    try:
        load_more = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'loadMoreBtn')))
        load_more.click()
        time.sleep(2)
    except:
        break
    

with open('yellow_pages_project/data.html','w') as file:
    file.write(driver.page_source)

driver.quit()