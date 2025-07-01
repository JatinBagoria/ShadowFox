from urllib.request import urlopen
import re

url = "https://books.toscrape.com/"
response = urlopen(url)
html = response.read().decode('utf-8')

# Regular expression to find book titles and prices
titles = re.findall(r'title="(.*?)"', html)
prices = re.findall(r'£\d+\.\d{2}', html)

# Print only matched pairs
for title, price in zip(titles[:20], prices[:20]):  # top 20 books
    print(f"📘 Book: {title} | 💰 Price: {price}")
