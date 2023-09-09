from bs4 import BeautifulSoup
import requests, selenium
from main import assitant
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from seleniumwire import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import vlc
import json, re


service = Service(
    executable_path="C:/Users/laziz/PycharmProjects/pet-projects/marketplace/parsing/parsing_products/chromedriver.exe"
)

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                     " (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
# options.headless = True
driver = webdriver.Chrome(service=service, options=options)
url = ("https://uz.wildberries.ru/catalog/elektronika/noutbuki-i"
       "-kompyutery/komplektuyushchie-dlya-pk?sort=popular&page=1")
driver.get(url=url)


page_height = driver.execute_script("return document.body.scrollHeight")


while True:
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    sleep(3)
    new_page_height = driver.execute_script("return document.body.scrollHeight")
    if new_page_height == page_height:
        break
    page_height = new_page_height

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
product_list = soup.find('div', class_='product-card-list')
product_card_wrapper = soup.find_all('div', class_="product-card__wrapper")

product_descriptions = []
count = 0
remained = len(product_card_wrapper)
for i in product_card_wrapper:
    count += 1
    remained -= 1
    product_name = i.find('h2', class_='product-card__brand-wrap').text
    product_image = i.find('img', class_='j-thumbnail').get('src')
    product_price_element = i.find('p', class_="product-card__price price").text.strip()
    product_price = int(product_price_element.split("сум")[0].strip().replace('\xa0', ''))
    product_link = i.find('a', class_='product-card__link j-card-link j-open-full-product-card').get('href')
    driver.get(product_link)
    try:
        product_description_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'collapsable__text'))
        )

        product_description = product_description_element.text
    except Exception as e:
        product_description = "Description not found"

    product_descriptions.append({
        'name': product_name,
        'image': product_image,
        'price': product_price,
        'description': product_description
    })
    assitant(f'Страниц обработано: {count}, осталось {remained}')

with open('C:/Users/laziz/PycharmProjects/pet-projects/marketplace/static/result_list.json', 'w', encoding='utf-8') as file:
    json.dump(product_descriptions, file, indent=4, ensure_ascii=False)

driver.close()
driver.quit()

p = vlc.MediaPlayer("zadaniye.mp3")
p.play()
