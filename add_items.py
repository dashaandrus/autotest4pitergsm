from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class NewItem:

    def __init__(self):
        self.watch_price_to_int = None
        self.watch_name_text = None
        self.iphone_price_to_int = None
        self.iphone_name_text = None

    def add_iphone_to_cart(self, driver):

        # Находим элемент, на который нужно навести
        menu_item_iphone = driver.find_element(By.XPATH, '//li[@id="bx_651765591_1673"]')

        # Выполняем наведение на элемент в выпадающем списке
        actions = ActionChains(driver)
        actions.move_to_element(menu_item_iphone).perform()

        # Кликаем по товару из выпадающего списка
        dropdown_iphone = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="bx_651765591_1673"]/div/div/div/ul/li[2]/a/span')))
        dropdown_iphone.click()

        # Выбираем фильтр по памяти
        button_iphone_memory = driver.find_element(By.XPATH, '//a[@href="/catalog/phones/iphone/iphone-17-pro-max/512gb/"]')
        button_iphone_memory.click()

        # Добавляем телефон в корзину
        add_iphone_to_cart = driver.find_element(By.XPATH, '(//button[@data-product-id="122715"])[3]')
        add_iphone_to_cart.click()

        # Запоминаем название и цену телефона для сравнения в корзине
        iphone_name = driver.find_element(By.XPATH, '(//a[@href="/catalog/phones/iphone/iphone-17-pro-max/esim/smartfon-apple-iphone-17-pro-max-esim-512gb-silver-serebristyy/"])[2]')
        self.iphone_name_text = iphone_name.text
        iphone_price = driver.find_element(By.XPATH, '(//div[@class="prodcard__price"])[3]')
        iphone_price_text = iphone_price.text
        self.iphone_price_to_int = int(iphone_price_text.replace(" ", "").replace("₽", "").strip())

    def add_watch_to_cart(self, driver):
        # Находим элемент для клика
        menu_item_watches = driver.find_element(By.XPATH, '//a[@href="/catalog/watch/"]')
        menu_item_watches.click()

        # Выбираем тип часов
        button_type_watch = driver.find_element(By.XPATH, '//a[@href="/catalog/watch/apple-watch/"]')
        button_type_watch.click()

        # Выбираем размер экрана часов
        button_watch_size = driver.find_element(By.XPATH,
                                                '//*[@id="page-side"]/div[2]/div[2]/div/div/div/label[4]/span/span')
        button_watch_size.click()

        # Листаем страницу и добавляем часы
        add_watch_to_cart = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '(//button[@data-product-id="40485"])[3]')))
        driver.execute_script("window.scrollTo(0, 2300);")
        add_watch_to_cart.click()

        # Запоминаем название и цену часов для сравнения в корзине
        watch_name = driver.find_element(By.XPATH,
                                         '(//a[@href="/catalog/watch/apple-watch/watch-hermes-series-10/apple-watch-hermes-series-10-42mm-silver-titanium-case-with-double-tour-attelage-etoupe/"])[2]')
        self.watch_name_text = watch_name.text
        watch_price = driver.find_element(By.XPATH, '//*[@id="catalog"]/div[14]/div[3]/div[1]/div[1]/span')
        watch_price_text = watch_price.text
        self.watch_price_to_int = int(watch_price_text.replace(" ", "").replace("₽", "").strip())

