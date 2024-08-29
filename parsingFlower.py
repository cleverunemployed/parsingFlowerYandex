# -*- coding: utf-8 -*-

import csv
import json
import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium_stealth import stealth


def parsing_links_goods() -> list[str]:
    
    # create a ChromeOptions object
    options = webdriver.ChromeOptions()

    #run in headless mode
    options.add_argument("--headless=new")

    # disable the AutomationControlled feature of Blink rendering engine
    options.add_argument('--disable-blink-features=AutomationControlled')

    # disable pop-up blocking
    options.add_argument('--disable-popup-blocking')

    # start the browser window in maximized mode
    options.add_argument('--start-maximized')

    # disable extensions
    options.add_argument('--disable-extensions')

    # disable sandbox mode
    options.add_argument('--no-sandbox')

    # disable shared memory usage
    options.add_argument('--disable-dev-shm-usage')

    #create a new driver instance
    driver = webdriver.Chrome(options=options)

    # Change the property value of the navigator for webdriver to undefined
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    # Step 3: Rotate user agents 
    user_agents = [
        # Add your list of user agents here
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    ]

    # select random user agent
    user_agent = random.choice(user_agents)

    # pass in selected user agent as an argument
    options.add_argument(f'user-agent={user_agent}')
    
    cookies = {
    'receive-cookie-deprecation': '1',
    'visits': '1724746981-1724746981-1724746981',
    'cmp-merge': 'true',
    'reviews-merge': 'true',
    'skid': '624638961724746981',
    'i': 'Z2Kx/V2N0yKh0RidrlaNItjHVEN1jsEFhDJFVoWpWTXdAuKK+NaKlmyOb9Arf7DKsaUdF1XiBDX6riaXrXmv5QBf3NQ=',
    'yashr': '1322175101724746981',
    'oq_shown_onboardings': '%5B%5D',
    'oq_last_shown_date': '1724746981309',
    'server_request_id_market:index': '1724746981268%2Fe3cfb40413f1046a7c5c25f3a5200600%2F1%2F1',
    'rcrr': 'true',
    'muid': '1152921512013669848%3A4NeHeaNYTl%2FOn5bwCClKblko0k4qfDDG',
    'i': '+r9BL3u3BPkHkmhPmDDkvyLX7445wY02Hm0dvJFqx0934Kn7KudR9vncVk93C+OzgthSOcpuXfQLTbqctIzi+f7mgNk=',
    'yandexuid': '5637393981724746981',
    'yashr': '3897751131724746981',
    'bh': 'EkIiQ2hyb21pdW0iO3Y9IjEyOCIsICJOb3Q7QT1CcmFuZCI7dj0iMjQiLCAiTWljcm9zb2Z0IEVkZ2UiO3Y9IjEyOCIqAj8wOgkiV2luZG93cyJg5Zm2tgZqIdzK4f8IktihsQOfz+HqA/v68OcN6//99g+2xsyHCJeyAg==',
    'gdpr': '0',
    'yandexuid': '5637393981724746981',
    'spvuid_market:index_3751af_expired:1724833383258': '1724746981268%2Fe3cfb40413f1046a7c5c25f3a5200600%2F1%2F1',
    'yuidss': '5637393981724746981',
    'spvuid_market:special_70440d_expired:1724833401344': '1724747001299%2F71e574553816d6f4e60057f4a5200600%2F1%2F1',
    'ygu': '0',
    'spvuid_market:list_5b52d5_expired:1724833444301': '1724747044261%2Fcb85c24c25211915d68ce6f6a5200600%2F1%2F1',
    'js': '1',
    'nec': '0',
    'is_gdpr': '0',
    'is_gdpr_b': 'CI6GJBDLjwI=',
    'ugcp': '1',
    '_yasc': 'XDLfFK9rlyTkskAgsq0HvX/G5i8lLeK8nfVOecx/4Uv6A9s4u0KS9Bpw5kT1l3hUWRl8RihHKw==',
    'yandexmarket': '48%2CRUR%2C1%2C%2C%2C%2C2%2C0%2C0%2C213%2C0%2C0%2C12%2C0%2C0',
    'yandex_gid': '213',
    'parent_reqid_seq': '1724747787603%2F8c31e7ff195f735c880f3523a6200600%2F1%2F1%2C1724747806489%2Faf854618adcf332bfe395524a6200600%2F1%2F1%2C1724755749479%2Fc1f11eda46e57ecc96a2c5fda7200600%2F1%2F1%2C1724756757869%2Fab875d8e1bdf78c89b73e039a8200600%2F1%2F1%2C1724757146524%2Faafb0cfe40fdcd238ada0a51a8200600%2F1%2F1',
    'global_delivery_point_skeleton': '{%22deliveryType%22:%22PICKUP%22%2C%22outletType%22:%22pickup%22%2C%22regionName%22:%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22addressLineWidth%22:269}',
    }
    
    for name in cookies.keys():
        driver.add_cookie({"name": name, "value": cookies[name], "domain": "market.yandex.ru"})

    # Step 4: Scrape using Stealth
    #enable stealth mode
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    
    driver.get("https://market.yandex.ru/catalog--avtorskie-bukety/30584411/list?hid=91284&rs=eJwz4g1g_MTIwcEgwaAw5SSrkw2XNBcHB6OAggSvAosAmxRnSmpaYmlOSbyRAoMGA1ySUYERWdIQJCnA5MWRbGZinmqZYhFkZGhuZGJuYm5gamFsaK6fZmRomWhukmKRYpmabG5olmxqYJ6UkmaeaGpkYGBmYKBvqG8IAAcRHEY%2C&glfilter=7893318%3A50059619")

    time.sleep(5)
    
    saveHtml(driver.page_source)
    
    driver.quit()
    
    return []


def saveHtml(html: str) -> None:
    with open("index.html", mode="w+", encoding="utf-8") as file:
        file.write(html)


def main():
    parsing_links_goods()


if __name__ == "__main__":
    main()
