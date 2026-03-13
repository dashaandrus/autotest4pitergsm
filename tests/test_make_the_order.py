from selenium.webdriver.common.by import By


class MakeOrder():

    button_make_order = By.XPATH, '//a[@href="/personal/order/make/"]'
    name = By.XPATH, '//input[@placeholder="Ф.И.О."]'
    email = By.XPATH, '//input[@placeholder="E-Mail"]'
    phone_number = By.XPATH, '//input[@placeholder="Телефон"]'
    comment = By.XPATH, '//textarea[@placeholder="Комментарий"]'
    button_cart = By.XPATH, '//span[@class="m-nowrap js-order-price"]'

    def test_make_the_order(self, driver, iphone_price_to_int, watch_price_to_int):

        make_order = driver.find_element(*self.button_make_order)
        make_order.click()

        customer_name = driver.find_element(*self.name)
        customer_name.send_keys('Тестов Тест Тестович')

        customer_email = driver.find_element(*self.email)
        customer_email.send_keys('test@email.ru')

        customer_phone_number = driver.find_element(*self.phone_number)
        customer_phone_number.send_keys('+79999999999')

        customer_comment = driver.find_element(*self.comment)
        customer_comment.send_keys('I love Python!')

        sum_cart_final = driver.find_element(*self.button_cart)
        sum_cart_final_text = sum_cart_final.text
        sum_cart_final_to_int = int(sum_cart_final_text.replace(" ", "").replace("₽", "").strip())

        assert sum_cart_final_to_int == (
                    watch_price_to_int + iphone_price_to_int), 'Oops! The total amount doesnt converge'
        print('The total amount converges')