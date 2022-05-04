# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
# from faker import Faker
from time import sleep

# TestData
username = "hanna.parchomenko@eracent.com"
haslo = "hp123!@#"

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Przygotowanie testu
        # Warunki wstępne testu
        # Otwarcie przeglądarki
        self.driver = webdriver.Chrome()
        # Otwarcie strony
        self.driver.get("https://itpedia.eracent.com")
        # Maksymalizacja okna
        self.driver.maximize_window()
        # Ustawienie bezwarunkowego czekania na elementy przy wyszukiwaniu
        # maks. 10 sekund
        self.driver.implicitly_wait(50)

        # Wlasciwy test
        # nazwa musi zaczynac sie od slowa test
    def testLogin(self):
        # 1. Wpisz UserName
        driver = self.driver
        username_input = driver.find_element(By.ID, "UserName")
        username_input.send_keys(username)

        # 2. Wpisz haslo
        haslo_input = driver.find_element(By.ID, "Password")
        haslo_input.send_keys(haslo)
        # 3. Kliknij Login

        driver.find_element(By.ID, "sub").click()

        # maks. 10 sekund
        self.driver.implicitly_wait(50)

        menu = driver.find_element(By.ID, 'sidebar')

        sleep(15)
