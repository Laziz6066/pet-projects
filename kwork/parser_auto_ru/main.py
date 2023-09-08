import asyncio
import pickle
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from seleniumwire import webdriver

PROXY = "KQqSdM:bPEYT5@45.10.249.143:8000"

async def fetch_data(page):
    service = Service(
        executable_path="C:/Users/laziz/PycharmProjects/pet-projects/kwork/parser_auto_ru/chromedriver.exe"
    )

    options = webdriver.ChromeOptions()

    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
    options.add_argument(f'--proxy-server={PROXY}')
    options.headless = True
    driver = webdriver.Chrome(service=service, options=options)

    url = f"https://auto.ru/cars/bmw/all/?page={page}"
    car_data = []

    try:
        driver.get(url)
        for cookie in pickle.load(open('cookies', 'rb')):
            driver.add_cookie(cookie)

        driver.refresh()

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        car_model = soup.find_all('div', class_='ListingItem ListingItem_ctbautoru128Exp')

        for i in car_model:
            try:
                car_name = i.find('h3', class_='ListingItemTitle ListingItem__title').text
            except AttributeError:
                car_name = "Нет модели."
            try:
                car_price = i.find('div', class_="ListingItemPriceNew__content-HAVf2").text
            except AttributeError:
                car_price = i.find('div', class_="ListingItemPrice ListingItem__price").text
            try:
                mileage = i.find('div', class_='ListingItem__kmAge').text
            except AttributeError:
                mileage = 'Нет пробега.'
            try:
                year = i.find('div', class_='ListingItem__year').text
            except AttributeError:
                year = 'Нет года выпуска.'

            car_data.append(
                {
                    "car_name": car_name,
                    "car_price": car_price,
                    "mileage": mileage,
                    "year": year
                }
            )

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    return car_data, page

async def write_to_csv(car_data, page):
    with open(f'data/auto_ru_bmw_{page}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "Модель",
                "Цена",
                "Пробег",
                "Год выпуска",
            )
        )
        for car in car_data:
            writer.writerow(
                (
                    car['car_name'],
                    car['car_price'],
                    car['mileage'],
                    car['year'],
                )
            )

async def main():
    tasks = []
    for page in range(1, 100):
        car_data, page_number = await fetch_data(page)
        await write_to_csv(car_data, page_number)
        print(f'{page_number}-страница обработана. Машин: {len(car_data)}')

if __name__ == "__main__":
    asyncio.run(main())
