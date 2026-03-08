from selenium.webdriver.common.by import By


class MakeOrder():
    def make_the_order(self, driver, iphone_price_to_int, watch_price_to_int):

        make_order = driver.find_element(By.XPATH, '//a[@href="/personal/order/make/"]')
        make_order.click()

        customer_name = driver.find_element(By.XPATH, '//input[@placeholder="Ф.И.О."]')
        customer_name.send_keys('Тестов Тест Тестович')

        customer_email = driver.find_element(By.XPATH, '//input[@placeholder="E-Mail"]')
        customer_email.send_keys('test@email.ru')

        customer_email = driver.find_element(By.XPATH, '//input[@placeholder="Телефон"]')
        customer_email.send_keys('+79999999999')

        comment = driver.find_element(By.XPATH, '//textarea[@placeholder="Комментарий"]')
        comment.send_keys('I love Python!')

        sum_cart_final = driver.find_element(By.XPATH, '//span[@class="m-nowrap js-order-price"]')
        sum_cart_final_text = sum_cart_final.text
        sum_cart_final_to_int = int(sum_cart_final_text.replace(" ", "").replace("₽", "").strip())

        assert sum_cart_final_to_int == (
                    watch_price_to_int + iphone_price_to_int), 'Oops! The total amount doesnt converge'
        print('The total amount converges')