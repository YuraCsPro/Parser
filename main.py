import requests
import lxml
from bs4 import BeautifulSoup

url = "https://cash-backer.club/shops"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

session = requests.session()

for j in range(1,62):
    print(f"PAGE = {j}")

    response = session.get(url, headers=header)
    print(response)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        allProduct = soup.find("div", class_="row col-lg-9 col-md-9 col-12")
        #print(allProduct)
        products = allProduct.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")

    for i in range(len(products)):
        try:
            title = products[i].find("div", class_="shop-title").text
            price = products[i].find("div", class_="shop-rate").text
            with open("product.txt","div",encoding="UTF-8") as file:
                file.write(f"{title} --->>> {price}\n")
            print(title, price)
        except:
            print(f" not for sale")