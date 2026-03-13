from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class MakeWishlist():

    locator_button_offer = By.XPATH, '//button[@aria-label="Next slide"]'
    locator_offer = By.XPATH, '//img[@alt="Aibi Pocket Pet"]'
    locator_wishlist_product = By.XPATH, '//button[@data-product-id="141600"]'
    locator_wishlist_name = By.XPATH, '//h1[@data-product-name="Умный карманный робот Aibi Pocket Pet, белый"]'
    locator_wishlist = By.XPATH, '//a[@id="header__favorites-counter"]'
    locator_wishlist_name_for_assert = By.XPATH, '//a[@class="prodcard__name"]'

    def test_make_wishlist(self, driver):
        # Находим элемент, на который нужно навести
        button_offer = driver.find_element(self.locator_button_offer)

        # Выполняем наведение на элемент в выпадающем списке
        actions = ActionChains(driver)
        actions.move_to_element(button_offer).perform()

        # Выполняем переключение стрелками в рекламных предложениях до нужного нам товара
        for i in range(0, 5):
            button_offer.click()
            time.sleep(2)

        # Кликаем на понравившуюся рекламу
        offer = driver.find_element(self.locator_offer)
        offer.click()

        # добавляем в избранное товар из рекламы
        wishlist_product = driver.find_element(self.locator_wishlist_product)
        wishlist_product.click()

        wishlist_name = driver.find_element(self.locator_wishlist_name)
        wishlist_name_text = wishlist_name.text

        # проверяем, что товар в вишлисте и именно тот, что мы добавляли

        wishlist = driver.find_element(self.locator_wishlist)
        wishlist.click()

        wishlist_name_for_assert = driver.find_element(self.locator_wishlist_name_for_assert)
        wishlist_name_for_assert_text = wishlist_name_for_assert.text

        assert wishlist_name_text == wishlist_name_for_assert_text, 'Oops! Thats not mine'
        print('Thats my wishlist item')