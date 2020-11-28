from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    driver = webdriver.Chrome(executable_path='/Users/oakhonov/PyCharmProjects/chromedriver')
    driver.wait = WebDriverWait(driver, 5)
    return driver


def get_headers(driver):
    driver.get(input('Введи ссылку на товар на сайте Мвидео. (Важно нужна ссылка на все характеристики):  '))
    elements = driver.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'h3')))
    return elements


def get_specification(driver):
    elements = driver.wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'table.table.table-striped.product-details-table')))
    return elements


def handle_data(headers, specification):
    counter = 1
    for element in specification:
        sub_element = element.find_elements(By.CLASS_NAME, 'product-details-overview-specification')
        print('-', headers[counter].text)
        counter += 1
        for num in range(0, len(sub_element), 2):
            print(sub_element[num].text)


if __name__ == "__main__":
    driver = init_driver()
    x = get_headers(driver)
    y = get_specification(driver)
    handle_data(x, y)
