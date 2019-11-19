import pandas as pd
from selenium import webdriver
from datetime import date
import random
import time


df = pd.read_excel('numbers.xlsx')
target_list = df['working column'].tolist()

driver = webdriver.Chrome('C:\\Users\Guja\Downloads\chromedriver')

driver.get('https://www.facebook.com/php')
email = 'guja1515@gmail.com'
password = '*your password here*'

driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()

z = 0

random = random.randint

result_list = list()

for x in target_list:
    if str(x) == 'nan':
        break
    time.sleep(random(10,30))
    target_url = str(x)
    driver.get(target_url)
    result_list.append(driver.current_url)
    z = z + 1
    print(z)
    while z == 20:
       print('break')
       time.sleep(random(600,1200))
       z = 0

export = pd.DataFrame(result_list, columns = ['Users'])

today = date.today()
print(today)

export.to_excel("new_acc's" + str(today) + ".xlsx")

print('Job Done')
