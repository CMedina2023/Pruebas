import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_uno():
    print("Prueba uno")


def test_dos():
    print("Prueba uno")


def test_tres():
    print("Prueba uno")


def test_login():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Habilita el modo headless
    chrome_options.add_argument('--disable-gpu')  # Desactiva la GPU para evitar problemas en algunos sistemas
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.google.com.mx')
    driver.quit()
