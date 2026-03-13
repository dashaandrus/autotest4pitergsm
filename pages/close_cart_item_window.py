from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Закрываем окно после добавления товара
class CLoseWindow():

    locator_close_adding_window = By.XPATH, '(//button[@class="popup__close js_popup_close isinit"])[7]'

    def test_close_window(self, driver):
        close_adding_window = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(self.locator_close_adding_window))
        close_adding_window.click()
