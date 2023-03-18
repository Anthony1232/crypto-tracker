from helium import *
from bs4 import BeautifulSoup as bs
import time
import atexit
import os

set_driver(f'{os.getcwd()}')

def check(webb):
    web = bs(webb.page_source, 'html.parser')
    content = web.find('tbody', {'class': 'css-0'})
    crypto_box = content.find_all('tr', {'role': 'row'})

    crypto_names = [x.find('p').string for x in crypto_box]
    crypto_shorts = [x.find('span').string for x in crypto_box]
    crypto_prices = [x.contents[3].contents[0].string for x in crypto_box]

    full_names = tuple(zip(crypto_names, crypto_shorts))
    full = tuple(zip(full_names, crypto_prices))
    full_tag = {}

    for names, prices in full:
        full_tag[f'{names[0]}/{names[1]}'] = prices

    return full_tag.items()


def main():
    web = start_chrome('https://crypto.com/price', headless = True)
    try:
        while True:
            os.system('cls')
            cryptos = check(web)
            print('please exit program with ctr+c\nfailure to do so will leave applications open\n\n')
            for name, price in cryptos:
                print(f'{name}: {price}')
            time.sleep(10)
    finally:
        os.system('close.bat')
        print('exiting now safe')

main()

