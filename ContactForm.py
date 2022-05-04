# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
# from faker import Faker
# from time import sleep

# Danetestowe
firstname = "ala"

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        # Przygotowanie testu
        # Warunki wstępne testu
        # Otwarcie przeglądarki
        self.driver = webdriver.Chrome()
        # Otwarcie strony
        self.driver.get("https://itpedia.eracent.com")
        # Maksymalizacja okna
        self.driver.maximize_window()
        # # 1. Kliknij „Accept”
        # driver.find_element(By.LINK_TEXT, "Accept").click()
        # # Ustawienie bezwarunkowego czekania na elementy przy wyszukiwaniu
        # # maks. 10 sekund
        self.driver.implicitly_wait(3)

    def test_ContactUs(self):
        # Faktyczny test
        driver = self.driver
        # Kroki
        # driver.find_element(By.XPATH, '//div[@class=" Subscription"]/p').click()
        # driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[2]/h5/a[2]")
        # driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/h5/a")
        driver.find_element(By.LINK_TEXT, 'Contact us').click()
        self.driver.implicitly_wait(20)
        firstname_input = driver.find_element(By.ID, 'FirstName')
        firstname_input.send_keys(firstname)

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()