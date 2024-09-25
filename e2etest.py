from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.keys import Keys

drive = webdriver.Chrome()

try:

    drive.get('https://www.saucedemo.com/')

    user_name = WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

    password = WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )

    user_name.send_keys("standard_user")
    password.send_keys("secret_sauce")

    password.send_keys(Keys.RETURN)

    WebDriverWait(drive, 10).until(
        EC.url_changes('https://www.saucedemo.com/')
    )

    WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    print("Вход выполнен успешно")

    drive.get('https://www.saucedemo.com/inventory.html')

    basket = WebDriverWait(drive, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )

    basket.click()


    WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    print("Товар добавлен в корзину")

    drive.get("https://www.saucedemo.com/cart.html")

    decoration = WebDriverWait(drive, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )

    decoration.click()

    print("Успешный переход на страницу оформления")

    drive.get("https://www.saucedemo.com/checkout-step-one.html")

    name = WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )

    last_name = WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.ID, "last-name"))
    )

    code_region = WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.ID, "postal-code"))
    )

    name.send_keys("Nikolay")
    last_name.send_keys("Ivanovich")
    code_region.send_keys("11111")

    continue_page = WebDriverWait(drive, 10).until(

        EC.element_to_be_clickable((By.ID, "continue"))
    )

    continue_page.click()

    print("Форма заполнена успешно")
    print("Переход на страницу покупки успешен")

    drive.get("https://www.saucedemo.com/checkout-step-two.html")

    buy = WebDriverWait(drive, 10).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )

    buy.click()

    print("Товар успешно куплен")

finally:
    drive.quit()




