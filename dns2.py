from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re


def init_driver():
    driver = webdriver.Chrome(executable_path='/Users/oakhonov/PyCharmProjects/chromedriver')
    driver.wait = WebDriverWait(driver, 5)
    return driver


def get_table(driver):
    driver.get(
        'https://www.dns-shop.ru/product/e110c867b4503330/zerkalnaa-kamera-nikon-d3500-kit-18-55mm-af-p-cernyj/characteristics/')
    elements = driver.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'table-params.table-no-bordered')))
    main_information = list(elements[0].text.split('\n'))
    return main_information


def get_headers(driver):
    headers = []
    elements = driver.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'table-part')))
    for element in elements:
        headers.append(element.text)
    return headers


def get_specification(driver):
    specification = []
    elements = driver.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'dots')))
    for element in elements:
        specification.append(element.text)
    return specification


def delete_redundant_info(table, headers, specification):
    final_list = []
    for item in table:
        if item in headers:
            final_list.append(item)
        elif item in specification:
            final_list.append(item)
        else:
            pass
    print(final_list)


if __name__ == '__main__':
    driver = init_driver()
    table = get_table(driver)
    headers = get_headers(driver)
    specification = get_specification(driver)
    delete_redundant_info(table, headers, specification)