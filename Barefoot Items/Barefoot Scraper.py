from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'Barefoot_items_data.csv')

url = 'https://barefootbuttons.com/product-category/version-1/'

session = HTMLSession()


def get_items_links():
    itemsValid = []

    r = session.get(url)
    items = r.html.find('a')

    for item in items:
        href_of_item = item.attrs['href']
        if "https://barefootbuttons.com/product/" in href_of_item:
            itemsValid.append(href_of_item)

    return list(dict.fromkeys(itemsValid))


def get_item_info(item_url):

    r = requests.get(item_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    item_title = soup.find('h1', class_='product-title').text
    item_price = soup.find_all('bdi')[1].text
    item_stock = soup.find('p', class_='stock').text
    item_sku = soup.find('span', class_='sku').text
    # item_tag = soup.find('a[rel=tag]')

    item = {
        'Title': item_title.strip(),
        'Price': item_price.strip(),
        'Stock': item_stock.strip(),
        'sku': item_sku.strip(),
        # 'tag: item_tag
        'url': item_url
    }

    return item


if __name__ == "__main__":

    links = get_items_links()
    items_data = []

    # Just scraping the first 5 links for learning purposes
    print('Just scraping the first 5 links for learning purposes')
    for itemURL in links[:5]:
        data = get_item_info(itemURL)
        items_data.append(data)
        print(f'{itemURL} scraped')

    df = pd.DataFrame(items_data)
    df.to_csv(output_path, index=False)

    print("Saving to Barefoot_items_data.csv SUCCESS !")
