from selenium.webdriver.common.by import By


class MainPage:

    locator_main_page = By.XPATH, '//img[@alt="PiterGSM"]'
# Выход на главную страницу сайта
    def test_return_to_main_page(self, driver, base_url):

        main_page = driver.find_element(*self.locator_main_page)
        main_page.click()
        get_url = driver.current_url

        assert get_url == base_url, 'Where are we...'
        print('We are on the main page!')