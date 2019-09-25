from selenium import webdriver
from bs4 import BeautifulSoup

path = 'C:/Users/gjb26/Desktop/chromedriver.exe'  # ex. C:/downloads/chromedriver.exe

# 조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
driver = webdriver.Chrome(path)

driver.get('https://ktis.kookmin.ac.kr/')
driver.implicitly_wait(3)
id = '20153159'
pw = 'rhrnak2628!'
driver.execute_script("document.getElementsByName('txt_user_id')[0].value=\'" + id + "\'")
# time.sleep(1)
driver.execute_script("document.getElementsByName('txt_passwd')[0].value=\'" + pw + "\'")
# time.sleep(1)

driver.find_element_by_xpath('/html/body/form[1]/table/tbody/tr/td/table/tbody/tr[4]/td[1]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/input').click()
driver.implicitly_wait(3)

driver.get('https://ktis.kookmin.ac.kr/kmu/ucb.Ucb0164rAGet01.do')
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
soup.prettify(formatter=lambda s: s.replace('&nbsp', ''))
notices = soup.findAll('td',attrs={'rowspan':'2'})
notices2 = soup.findAll('td',attrs={'rowspan':'3'})

# for n in notices:
#     print(n.text)

for n in notices2:
    print(n.text)
