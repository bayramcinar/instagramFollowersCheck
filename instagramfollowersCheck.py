from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pwinput
import time


kullaniciAdi = input("kullanıcı adını gir: ")
sifre = pwinput.pwinput(prompt='Şifre: ')
kisi = input("Takipçilerini göndermek istediğiniz kişinin kullanıcı adı: ")


chrome_driver_path = "C:\drivers\chromedriver"

driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(10)

url = "https://www.instagram.com/"


driver.get(url)


username = driver.find_element(By.NAME,"username")
username.send_keys(kullaniciAdi)

password = driver.find_element(By.NAME,"password")
password.send_keys(sifre)
password.send_keys(Keys.ENTER)


notnow = driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div/div/button')
notnow.click()


notnow1 = driver.find_element(By.XPATH,'/html/body')
notnow1.click()


notnow2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
notnow2.click()


search = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/input")
search.send_keys(kisi)

select = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/a")
select.click()

followers = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a")
followers.click()

modal = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div')


count = len(driver.find_elements(By.CSS_SELECTOR,"._aacl._aaco._aacw._aacx._aad7._aade"))

f = []


max = 100000
while count<max:
    modal.click()

    element = driver.find_element(By.TAG_NAME,"html")
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

    element = driver.find_element(By.TAG_NAME,"html")
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    
    element = driver.find_element(By.TAG_NAME,"html")
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    
    element = driver.find_element(By.TAG_NAME,"html")
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

    element = driver.find_element(By.TAG_NAME,"html")
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    
    element = driver.find_element(By.TAG_NAME,"html")
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

    element = driver.find_element(By.TAG_NAME,"html")
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

    element = driver.find_element(By.TAG_NAME,"html")
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

    element = driver.find_element(By.TAG_NAME,"html")
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

    element = driver.find_element(By.TAG_NAME,"html")
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    
    
    
    newCount = len(driver.find_elements(By.CSS_SELECTOR,"._aacl._aaco._aacu._aacx._aada"))

    time.sleep(0.5)
    
    if count != newCount:
        count = newCount
    
    else:
        break    
likers = driver.find_elements(By.CSS_SELECTOR,"._aacl._aaco._aacu._aacx._aada")
for like in likers:
    f.append(like.text)

i = 1    
for followers in f:
    print(f"{i}-{followers}")
    i=i+1
print(f"total followers is : {len(f)}")    