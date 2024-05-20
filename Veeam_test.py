from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
import time

driver = webdriver.Edge()

print('Search vacancies at Veeam')
x = input('Enter department: ')
a = input('Enter Country: ')

def do_count():
  global count
  count = len(driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[1]/div[1]/div/div[2]/a/div[2]/h5'))

  if count == 1:
    print(str(count) + ' open position.')
  else:
    print(str(count) + ' open positions.')

def do_comp():

  comp = (count/count)
  per = f"{comp:.0%}"
  print(per + ' of vacancies counted.')

def do_search():
  global b
  b = input('Enter City: ')
  
  driver.maximize_window()
  driver.get('https://careers.veeam.com/vacancies')

  try:
    driver.find_element(By.ID,'department-toggler').click()
    driver.find_element(By.LINK_TEXT, x).click()
  
    time.sleep(6)

    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/header/div/div/div[3]/div[1]/div/button').click()
    driver.find_element(By.LINK_TEXT, a).click()
    time.sleep(6)

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/header/div/div/div[3]/div[2]/div/button').click()
    driver.find_element(By.LINK_TEXT, b).click()
    time.sleep(6)

    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/header/div/div/div[4]/button[1]').click()
    time.sleep(6)

    do_count()

    if count >=1:
      do_comp()

  except NoSuchElementException:
    print('No vacancies in the desired department or location')

def do_search_us():
  global b
  a = 'USA'
  c = input('Enter State: ')
  b = input('Enter City: ')
  driver.maximize_window()
  driver.get('https://careers.veeam.com/vacancies')

  try:
    driver.find_element(By.ID,'department-toggler').click()
    driver.find_element(By.LINK_TEXT, x).click()

    time.sleep(6)

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/header/div/div/div[4]/div[1]/div/div/button').click()
    driver.find_element(By.LINK_TEXT, c).click()
    time.sleep(6)

    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/header/div/div/div[4]/div[2]/div/button').click()
    driver.find_element(By.LINK_TEXT, b).click()
    time.sleep(6)

    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/header/div/div/div[4]/button[1]').click()

    do_count()

    if count >=1:
      do_comp()

  except NoSuchElementException:
    print('No vacancies in the desired department or location')

USA = {'US', 'America', 'States', 'United States', 'USA'}

if a in USA:
  do_search_us()  

else:
  do_search()

 


    



