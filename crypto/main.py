import os
import atexit
import time

try:
    from helium import *
    from bs4 import BeautifulSoup as bs
except:
    s = input('click enter to install helium + beautifulsoup (required python libraries)\n')
    os.system('cmd /c "pip install helium"')
    os.system('cmd /c "pip install BeautifulSoup4"')
    from helium import *
    from bs4 import BeautifulSoup as bs

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
            printer = '''\nplease exit program with ctr+c\nfailure to do so will leave applications open\n\n'''
            for name, price in cryptos:
                printer += f'\n{name}: {price}'
            print(printer)
            time.sleep(10)
    finally:
        os.system('close.bat')
        print('exiting now safe')

main()

