from selenium.webdriver.common.by import By

class CheckCart():

    locator_personal_cart = By.XPATH, '(//a[@href="/personal/cart/"])[2]'
    locator_first_item = By.XPATH, '(//a[@href="/catalog/phones/iphone/iphone-17-pro-max/esim/122715/"])[2]'
    locator_first_item_price = By.XPATH, '(//div[@class="cart-prodcard__price-current"])[1]'
    locator_second_item = By.XPATH, '(//a[@href="/catalog/watch/apple-watch/watch-hermes-series-10/40485/"])[2]'
    locator_second_item_price = By.XPATH, '(//div[@class="cart-prodcard__price-current"])[2]'
    locator_sum_cart = By.XPATH, '//div[@class="total__price"]'

    def test_check_cart(self, driver, iphone_price_to_int, watch_price_to_int, iphone_name_text, watch_name_text):

        personal_cart = driver.find_element(self.locator_personal_cart)
        personal_cart.click()

        # Получаем наименование и цену товаров в корзине
        first_item = driver.find_element(self.locator_first_item)
        first_item_text = first_item.text
        first_item_price = driver.find_element(self.locator_first_item_price)
        first_item_price_text = first_item_price.text
        first_item_price_to_int = int(first_item_price_text.replace(" ", "").replace("₽", "").strip())

        second_item = driver.find_element(self.locator_second_item)
        second_item_text = second_item.text
        second_item_price = driver.find_element(self.locator_second_item_price)
        second_item_price_text = second_item_price.text
        second_item_price_to_int = int(second_item_price_text.replace(" ", "").replace("₽", "").strip())

        # Получаем сумму корзины
        sum_cart = driver.find_element(self.locator_sum_cart)
        sum_cart_text = sum_cart.text
        sum_cart_to_int = int(sum_cart_text.replace(" ", "").replace("₽", "").strip())

        # Сравниваем сумму и наименования
        assert first_item_price_to_int == iphone_price_to_int, 'Oops! The iphone amount doesnt converge'
        assert second_item_price_to_int == watch_price_to_int, 'Oops! The watch amount doesnt converge'
        assert sum_cart_to_int == (
                    watch_price_to_int + iphone_price_to_int), 'Oops! The total amount doesnt converge'
        print('The total amount converges')
        assert first_item_text == f'{"Смартфон "}{iphone_name_text}', 'Oops! Thats not my Iphone!'
        print('Thats my Iphone')
        assert watch_name_text == second_item_text, 'Oops! Thats not my watch!'
        print('Thats my Watches')