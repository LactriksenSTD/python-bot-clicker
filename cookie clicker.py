from selenium import webdriver
import time

window = webdriver.Chrome("C:\chromedriver.exe")
window.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(1)

cookie = window.find_element_by_xpath("/html/body/div[2]/div[2]/div[15]/div[8]/div[1]")
shop_products = window.find_elements_by_xpath("/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/*")
shop_products.reverse()

clicks = 0

def buy_items():
    buy_more = False
    for item in shop_products:
        if item.get_attribute("class") == "product unlocked enabled":
            item.click()
            buy_more = True
            break
        if buy_more is True:
            buy_items()

while True:
    cookie.click()
    clicks += 1
    if clicks == 100:
        buy_items()
        clicks = 0
