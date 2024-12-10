import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

pages = 1

chrome_options = Options()
chrome_options.add_argument("--headless=new") # for Chrome >= 109

driver = webdriver.Chrome(options=chrome_options)

# products_links = []
links = []
count = 0

for page_number in range(pages):
    if page_number < 15:
        
        url = f"https://alwastta.com/categories/174667/%D8%A3%D8%B4%D9%85%D8%BA%D8%A9-%D9%88-%D8%BA%D8%AA%D8%B1?page=15"
        print("="*40)
        print(f'getting page:{ page_number + 1} products links ...')
        driver.get(url)

        time.sleep(2)
        # links = driver.find_elements(By.CSS_SELECTOR, ".row.products-list .prod-col.prod-col-tb a")

        
        flag = 0
        for flag in range(19):
            selector = f"#products-list > div:nth-child({flag+ 1}) > div > a"
            link = driver.find_element(By.CSS_SELECTOR, selector)
            li = link.get_attribute('href')
            links.append(li)
            print('Link Added.')
            count = count + 1

        
        page_number = page_number + 1

print(f"items count: {count}")
print("="*40)

items = [['رابط المنتج' ,'اسم المنتج', 'السعر', "وصف المنتج", "روابط الصور"]]
c_product = 1
for link in links: 
    # opening product link
    print("="*40)
    print(f'Opening product-{c_product} link: {link} ...')
    c_product = c_product + 1
    driver.get(link)
    time.sleep(2)

    # finding product data :
    carrosel = driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div/div[2]')
    images = carrosel.find_elements(By.TAG_NAME, 'img')
    title = driver.find_element(By.CSS_SELECTOR, "h1")
    price = driver.find_element(By.CSS_SELECTOR, ".product-formatted-price.theme-text-primary")
    descriptions = driver.find_elements(By.CSS_SELECTOR, ".col-lg-6.col-product-info  p")

    images_urls = []
    for image in images:
        print(image.get_attribute('src'))
        images_urls.append(image.get_attribute('src'))
    print(f"title: {title.text}")
    print(f"price: {price.text}")
    for desc in descriptions:
        print(desc.text)

    res = ''
    for s in descriptions:
        res += s.text + ' '
    
    url = ''
    for u in images_urls:
        url += u +  '\n'
    
    i = [link, title.text, price.text ,res , url]
    items.append(i)
    print(i)
    print(f'{title.text} Added.')

print(items)
driver.quit()

print(">>>>>>>>>>>>>>>>>>>>>>>")
print("saving data to csv ...")

df = pd.DataFrame(items[1:], columns=items[0])
df.to_csv("items1.csv", index=False)

print("csv saved .")
print(">>>>>>>>>>>>>>>>>>>>>>>")