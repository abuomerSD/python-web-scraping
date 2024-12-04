import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://mlika-sa.com/category/mQEbaz"

browser = webdriver.Firefox()
browser.get(url)

time.sleep(10)

pages = 5
page_delay = 5

for i in range(pages):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(page_delay)
    print(f"page {i+1} of {pages}")


box = browser.find_elements(By.TAG_NAME, "custom-salla-product-card")


items = [
    ["رابط المنتج" ,"رابط الصورة" , "اسم المنتج", "السعر", "الوصف", "المقاس"]
]

items_urls = {}

n = 0
for card in box:
    item = browser.find_element(By.CLASS_NAME, "product-card__image")
    imgUrl = card.find_element(By.TAG_NAME, "img").get_attribute("src")
    itemUrl = card.find_element(By.CSS_SELECTOR, ".product-card__image a").get_attribute("href")
    items_urls[itemUrl] = imgUrl
    n = n + 1

print(f"we have: {n} products in this category")

browser.quit()

newBrowser = webdriver.Firefox()

flag = 0


for i in items_urls:

    newBrowser.get(i)
    time.sleep(5)
    print("=============")
    print(f"product: {flag + 1}")
    print(i)
    
    title = newBrowser.find_element(By.CSS_SELECTOR, "body h1")
    price = newBrowser.find_element(By.CSS_SELECTOR, "body h4")

    if price.text == "":
        price = newBrowser.find_element(By.CSS_SELECTOR, "body h2")

    description = newBrowser.find_element(By.CSS_SELECTOR, "article")
    size = newBrowser.find_element(By.CSS_SELECTOR, "select")

    print(f"title:  {title.text}")
    print(f"price:  {price.text}")
    print(f"description:  {description.text}")
    print(f"size:  {size.text}")
    flag = flag + 1

    items.append([i, items_urls.get(i), title.text, price.text , description.text, size.text])



newBrowser.quit()

print("saving data to csv ...")

df = pd.DataFrame(items[1:], columns=items[0])
df.to_csv("items.csv", index=False)

print("csv saved .")
print(">>>>>>>>>>>>>>>>>>>>>>>")