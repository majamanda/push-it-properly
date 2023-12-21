import requests
from bs4 import BeautifulSoup

# url = "https://us.hay.com/furniture-groups/quilton-sofa/2530324.html?lang=en_US"
url = "https://www.theonlinefurniturestore.co.uk/sofas/olivia-empress-sofa-neptune-furniture"
# <h2 id="base-product-price" style="display: inline;" data-price="4350.000" class="price" itemprop="price" content="4350.000" data-default-value="£4,350.00">£4,350.00</h2>
request = requests.get(url)
content = request.content

soup = BeautifulSoup(content, "html.parser")
# element = soup.find("span", {"class": "value", "itemprop": "price"})
element = soup.find("h2", {"id": "base-product-price", "class": "price", "itemprop": "price"})

# print(content)

priceStr = (element.text.strip())
price = float(priceStr[1:].replace(",", ""))
# print(priceStr.replace(",", ""))
# print(price)
# price += 1000
if price < 5000:
    print("The price of the chair is: {}".format(priceStr))
    print("Fair enough. You can buy it!")
else:
    print("The price of the chair is: {}".format(price))
    print("Too expensive. Do not buy it!")
