from selenium.webdriver.common.by import By


class MainPage:
# Выход на главную страницу сайта
    def return_to_main_page(self, driver, base_url):

        main_page = driver.find_element(By.XPATH, '//img[@alt="PiterGSM"]')
        main_page.click()
        get_url = driver.current_url

        assert get_url == base_url, 'Where are we...'
        print('We are on the main page!')