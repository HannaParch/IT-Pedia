# Import bibliotek
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import unittest
from time import sleep
from selenium.webdriver.common.keys import Keys

# TestData
username = "hanna.parchomenko@eracent.com"
haslo = "hp123!@#"

invalidusername = "antoni"
haslo2 = "123456"
krotkiehaslo = "1a2"

produktdefinition = "sql server 2016"
error_invalid = "Incorrect username or password."
password_error = "The Password must be at least 6 characters long."


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
        self.driver.implicitly_wait(10)

        # Wlasciwy test
        # 3 przypadki testowe dotyczace logowania
        # 001 logowanie zakonczone powodzeniem
    def test_sign_in_with_valid_user(self):
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
        self.driver.implicitly_wait(10)
        driver.find_element(By.ID, 'sidebar')
        sleep(5)

        # Akceptowanie ciasteczek
        # Kliknij „Accept”
        driver.find_element(By.ID, "consent").click()

        # 002 logowanie bez powodzenia "Incorrect username or password"
    def test_sign_in_with_invalid_user(self):
        # 1. Wpisz niepoprawny UserName
        driver = self.driver
        username_input = driver.find_element(By.ID, "UserName")
        username_input.send_keys(invalidusername)

        # 2. Wpisz haslo
        haslo_input = driver.find_element(By.ID, "Password")
        haslo_input.send_keys(haslo2)

        # 3. Kliknij Login
        driver.find_element(By.ID, "sub").click()

        # maks. 10 sekund
        sleep(10)
        error = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/form/div[1]')
        error.get_attribute("value")
        self.assertEqual(error_invalid, error.text)
        print("komunikat prawidlowy: Incorrect username or password.")

        # 003 logowanie bez powodzenia "The Password must be at least 6 characters long."
    def test_sign_in_with_invalid_password(self):
        # 1. Wpisz poprawny UserName
        driver = self.driver
        username_input = driver.find_element(By.ID, "UserName")
        username_input.send_keys(username)

        # 2. Wpisz haslo krotsze niz 6 znakow
        haslo_input = driver.find_element(By.ID, "Password")
        haslo_input.send_keys(krotkiehaslo)

        # 3. Kliknij Login
        driver.find_element(By.ID, "sub").click()

        # maks. 10 sekund
        sleep(10)
        passwordinvalid = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/form/div[2]/div/span/span')
        passwordinvalid.get_attribute("value")
        self.assertEqual(password_error, passwordinvalid.text)
        print("komunikat prawidlowy: The Password must be at least 6 characters long")

        # 004 przypadek dotyczy wyszukiwania na stronie
    def test_search_by_category(self):
        # Logowanie
        # 1. Wpisz UserName
        driver = self.driver
        username_input = driver.find_element(By.ID, "UserName")
        username_input.send_keys(username)

        # 2. Wpisz haslo
        haslo_input = driver.find_element(By.ID, "Password")
        haslo_input.send_keys(haslo)

        # 3. Kliknij Login
        driver.find_element(By.ID, "sub").click()
        sleep(5)

        # Akceptowanie ciasteczek
        # Kliknij „Accept”
        driver.find_element(By.ID, "consent").click()

        # wyswietlanie szukanych Katalogow
        # Wyszukiwanie Catalogow po MfgProdNo
        driver.find_element(By.CLASS_NAME, "nav-link").click()
        sleep(5)
        MfgProdNo = driver.find_element(By.CLASS_NAME, "k-input")
        MfgProdNo.send_keys("77771")
        sleep(5)
        MfgProdNo.send_keys(Keys.RETURN)
        sleep(5)

        # Liczba produktw
        ListaCatalogow = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[4]/span[2]')
        ListaCatalogow.get_attribute("value")
        print("wynik wyszukiwania ", ListaCatalogow.text)


        # 005 Przejscie do menu zalogowanego uzytkownika i sprawdzenie jego nazwy i statusu
        # kliknij menu uzytkownika
        driver.find_element(By.CLASS_NAME, "btn-group").click()
        sleep(5)
        # wybierz opcje zarzadznia kontem
        driver.find_element(By.CLASS_NAME, "pr-3").click()
        sleep(5)

        # sprawdzenie biezacego uzytkownika
        # przejdz na zakladke User
        UserName = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div[2]/h4/strong')
        UserName.get_attribute("value")
        self.assertEqual(username, UserName.text)
        print("aktywny user", UserName.text)

        # 006 Przejscie do zakadki Subskrypcji i sprawdzenie statusu
        driver.find_element(By.ID, "tabstrip-tab-3").click()
        sleep(5)
        status = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[4]/div/div/div[1]/div[2]/div/div/div[1]/h5/span')
        status.get_attribute("value")
        print("status: ", status.text)

        # 007 Wylogowanie uzytkownika
        # kliknij menu uzytkownika
        driver.find_element(By.CLASS_NAME, "btn-group").click()
        sleep(5)

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/span/nav/div/div/ul[2]/li[2]/div/form/div/div/div[8]/a/div[2]/span').click()
        driver.find_element(By.ID, "welcome-logo")
        print("jestes na stronie startowej")
        sleep(5)

    def tearDown(self):
        # Zakończenie testu
        # Wyłączenie przeglądarki
        self.driver.quit()

if __name__ == 'main':
     unittest.main