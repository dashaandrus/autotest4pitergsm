from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class MakeWishlist():
    def make_wishlist(self, driver):
        # Находим элемент, на который нужно навести
        button_offer = driver.find_element(By.XPATH, '//button[@aria-label="Next slide"]')

        # Выполняем наведение на элемент в выпадающем списке
        actions = ActionChains(driver)
        actions.move_to_element(button_offer).perform()

        # Выполняем переключение стрелками в рекламных предложениях до нужного нам товара
        for i in range(0, 5):
            button_offer.click()
            time.sleep(2)

        # Кликаем на понравившуюся рекламу
        offer = driver.find_element(By.XPATH, '//img[@alt="Aibi Pocket Pet"]')
        offer.click()

        # добавляем в избранное товар из рекламы
        wishlist_product = driver.find_element(By.XPATH, '//button[@data-product-id="141600"]')
        wishlist_product.click()

        wishlist_name = driver.find_element(By.XPATH,
                                            '//h1[@data-product-name="Умный карманный робот Aibi Pocket Pet, белый"]')
        wishlist_name_text = wishlist_name.text

        # проверяем, что товар в вишлисте и именно тот, что мы добавляли

        wishlist = driver.find_element(By.XPATH, '//a[@id="header__favorites-counter"]')
        wishlist.click()

        wishlist_name_for_assert = driver.find_element(By.XPATH, '//a[@class="prodcard__name"]')
        wishlist_name_for_assert_text = wishlist_name_for_assert.text

        assert wishlist_name_text == wishlist_name_for_assert_text, 'Oops! Thats not mine'
        print('Thats my wishlist item')