from selenium.webdriver.common.by import By

class CompareItems():

    def compare_items(self, driver):
        driver.execute_script("window.scrollTo(0, 300);")
        product_1 = driver.find_element(By.XPATH, '(//button[@data-product-id="30110"])[2]')
        product_name_1 = driver.find_element(By.XPATH,
                                             '(//a[@href="/catalog/pristavki-i-igry/sony-playstation/sony-playstation-5/30110/"])[2]')
        product_name_1_text = product_name_1.text
        product_1.click()

        product_2 = driver.find_element(By.XPATH, '(//button[@data-product-id="70031"])[2]')
        product_name_2 = driver.find_element(By.XPATH,
                                             '(//a[@href="/catalog/pristavki-i-igry/nintendo-switch/nintendo-switch-2/70031/"])[2]')
        product_name_2_text = product_name_2.text
        product_2.click()

        driver.execute_script("window.scrollTo(0, 0);")
        button_slide_menu = driver.find_element(By.XPATH, '//label[@class="burger header__toggle-trigger"]')
        button_slide_menu.click()
        button_compare = driver.find_element(By.XPATH, '/html/body/div[3]/header/div[1]/div/nav/ul/li[2]/a/span[2]')
        button_compare.click()

        compare_product_name_1 = driver.find_element(By.XPATH,
                                                     '(//a[@href="/catalog/pristavki-i-igry/sony-playstation/sony-playstation-5/30110/"])[2]')
        compare_product_name_1_text = compare_product_name_1.text
        compare_product_name_2 = driver.find_element(By.XPATH,
                                                     '(//a[@href="/catalog/pristavki-i-igry/nintendo-switch/nintendo-switch-2/70031/"])[2]')
        compare_product_name_2_text = compare_product_name_2.text

        assert product_name_1_text == compare_product_name_1_text, 'Oops! Thats not mine'
        print('Thats my first compare item')
        assert product_name_2_text == compare_product_name_2_text, 'Oops! Thats not mine'
        print('Thats my second compare item')