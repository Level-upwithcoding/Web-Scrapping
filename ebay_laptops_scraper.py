import requests
from bs4 import BeautifulSoup
import pandas as pd

laptops_data = {
    "name": [],
    "price": [],
    "shipping": [],
    "link": []
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.ebay.com/'
}


page_no = 1
while True:
    print(page_no)
    page_url = f"https://www.ebay.com/sch/i.html?_dcat=177&_fsrp=1&_from=R40&_nkw=laptop&_sacat=0&RAM%2520Size=32%2520GB&Hard%2520Drive%2520Capacity=1%2520TB&_pgn={page_no}&rt=nc"
    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    if response.status_code != 200:
        continue

    next_page = soup.find("a", class_="pagination__next")

    if not next_page:
        break
    else:
        page_divs = soup.find("div", class_="srp-river-results")
        laptops = page_divs.find_all("div", class_="s-item__info")
        for laptop in laptops:
            if laptop.find("span", attrs={"role": "heading"}) is not None:
                name = laptop.find("span", attrs={"role": "heading"}).text
                laptops_data["name"].append(name)
            else:
                name = "No info"
                laptops_data["name"].append(name)

            if laptop.find("span", class_="s-item__price") is not None:
                price = laptop.find("span", class_="s-item__price").text
                laptops_data["price"].append(price)
            else:
                price = "No info"
                laptops_data["price"].append(price)
            if laptop.find("span", class_="s-item__shipping") is not None:
                shipping = laptop.find("span", class_="s-item__shipping").text
                laptops_data["shipping"].append(shipping)
            else:
                shipping = "No info"
                laptops_data["shipping"].append(shipping)
            if laptop.find("a", class_="s-item__link")["href"] is not None:
                link = laptop.find("a", class_="s-item__link")["href"]
                laptops_data["link"].append(link)
            else:
                link = "No info"
                laptops_data["link"].append(link)

    page_no += 1


df = pd.DataFrame(laptops_data)
df.to_excel("Laptops.xlsx")
