from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")

browser = webdriver.Chrome("/usr/local/bin/chromedriver",chrome_options=chrome_options)
browser.get("https://web.whatsapp.com")

wait = WebDriverWait(browser,600)

with open('my_wa_contacts.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
      if line_count == 0:
          print ("this is header column csv, none we do here")
          line_count += 1
      else:
          target = '"{}"'.format(row[0])
          string_message = row[1]

          # select destination goes here
          x_arg = '//span[contains(@title, ' + target + ')]'
          target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
          target.click()

          # sending the message goes here
          input_box = browser.find_element_by_class_name('p3_M1')
          input_box.send_keys(string_message + Keys.ENTER)
          line_count += 1

#browser.close()
