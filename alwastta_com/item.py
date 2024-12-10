import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = "https://alwastta.com/products/%D8%B4%D9%85%D8%A7%D8%BA-%D8%B4%D8%AA%D9%88%D9%8A-%D9%87%D8%B4%D8%AA%D8%A7%D8%AC"

chrome_options = Options()
# chrome_options.add_argument("--headless=new") # for Chrome >= 109

driver = webdriver.Chrome(options=chrome_options)

print("Opening browser...")
driver.get(url)


# =========================================
selector = "#wrap > div > div > div.row.lg-thumbs.d-lg-flex.product-images-carousel-thumbs"
#wrap .row > div > div > div.row.lg-thumbs.d-lg-flex.product-images-carousel-thumbs
print("Page Loading...")
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# div = driver.find_element(By.CSS_SELECTOR, selector)
# print(div.text)


# images = div.find_elements(By.TAG_NAME, 'img')
# for image in images:
#     print(image.text)
#     print(image.get_attribute('href'))

# image = driver.find_element(By.CSS_SELECTOR, ".row.lg-thumbs.d-lg-flex.product-images-carousel-thumbs.col-3.box-1-1.content.d-flex align-items-center.justify-content-center.thumb-image-a img")
carrosel = driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div/div[2]')
images = carrosel.find_elements(By.TAG_NAME, 'img')
title = driver.find_element(By.CSS_SELECTOR, "h1")
price = driver.find_element(By.CSS_SELECTOR, ".product-formatted-price.theme-text-primary")
descriptions = driver.find_elements(By.CSS_SELECTOR, ".col-lg-6.col-product-info  p")

for image in images:
    print(image.get_attribute('src'))
print(f"title: {title.text}")
print(f"price: {price.text}")
for desc in descriptions:
    print(desc.text)

time.sleep(2)
driver.quit()