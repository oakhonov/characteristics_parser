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


def get_all_elements(driver):
    elements = driver.find_elements_by_xpath('//*[@id]')
    all_elements = []
    for el in elements:
        attribute = el.get_attribute('id')
        all_elements.append(attribute)
    return all_elements


def handle_all_element(all_elements):
    id_locators = []
    pattern = 'pcv-\w+'
    for element in all_elements:
        pcv_element = re.search(pattern, element)
        if pcv_element is None:
            pass
        else:
            id_locators.append(pcv_element.group())
    return id_locators


def handle_id_locators(id_locators, driver):
    id_names = []

    element = driver.find_element_by_id('pcv-6YVW0')
    id_names.append(element.text)

    print(id_names)


#def get_description(driver):
 #   elements = driver.wait.until(
  #      EC.presence_of_all_elements_located((By.CLASS_NAME, 'table-part')))
   # return (elements)


if __name__ == "__main__":
    driver = init_driver()
    get_table(driver)
    all_elements = get_all_elements(driver)
    kk = handle_all_element(all_elements)
    handle_id_locators(kk, driver)