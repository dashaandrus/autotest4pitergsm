from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class NewItem:

    locator_menu_item_iphone = By.XPATH, '//li[@id="bx_651765591_1673"]'
    locator_dropdown_iphone = By.XPATH, '//*[@id="bx_651765591_1673"]/div/div/div/ul/li[2]/a/span'
    locator_button_iphone_memory = By.XPATH, '//a[@href="/catalog/phones/iphone/iphone-17-pro-max/512gb/"]'
    locator_add_iphone_to_cart = By.XPATH, '(//button[@data-product-id="122715"])[3]'
    locator_iphone_name = By.XPATH, '(//a[@href="/catalog/phones/iphone/iphone-17-pro-max/esim/smartfon-apple-iphone-17-pro-max-esim-512gb-silver-serebristyy/"])[2]'
    locator_iphone_price = By.XPATH, '(//div[@class="prodcard__price"])[3]'
    locator_menu_item_watches = By.XPATH, '//a[@href="/catalog/watch/"]'
    locator_button_type_watch = By.XPATH, '//a[@href="/catalog/watch/apple-watch/"]'
    locator_button_watch_size = By.XPATH, '//*[@id="page-side"]/div[2]/div[2]/div/div/div/label[4]/span/span'
    locator_add_watch_to_cart = By.XPATH, '(//button[@data-product-id="40485"])[3]'
    locator_watch_name = By.XPATH, '(//a[@href="/catalog/watch/apple-watch/watch-hermes-series-10/apple-watch-hermes-series-10-42mm-silver-titanium-case-with-double-tour-attelage-etoupe/"])[2]'
    locator_watch_price = By.XPATH, '//*[@id="catalog"]/div[14]/div[3]/div[1]/div[1]/span'

    def __init__(self):
        self.watch_price_to_int = None
        self.watch_name_text = None
        self.iphone_price_to_int = None
        self.iphone_name_text = None

    def test_add_iphone_to_cart(self, driver):

        # Находим элемент, на который нужно навести
        menu_item_iphone = driver.find_element(*self.locator_menu_item_iphone)

        # Выполняем наведение на элемент в выпадающем списке
        actions = ActionChains(driver)
        actions.move_to_element(menu_item_iphone).perform()

        # Кликаем по товару из выпадающего списка
        dropdown_iphone = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(self.locator_dropdown_iphone))
        dropdown_iphone.click()

        # Выбираем фильтр по памяти
        button_iphone_memory = driver.find_element(*self.locator_button_iphone_memory)
        button_iphone_memory.click()

        # Добавляем телефон в корзину
        add_iphone_to_cart = driver.find_element(*self.locator_add_iphone_to_cart)
        add_iphone_to_cart.click()

        # Запоминаем название и цену телефона для сравнения в корзине
        iphone_name = driver.find_element(*self.locator_iphone_name)
        self.iphone_name_text = iphone_name.text
        iphone_price = driver.find_element(*self.locator_iphone_price)
        iphone_price_text = iphone_price.text
        self.iphone_price_to_int = int(iphone_price_text.replace(" ", "").replace("₽", "").strip())

    def test_add_watch_to_cart(self, driver):
        # Находим элемент для клика
        menu_item_watches = driver.find_element(*self.locator_menu_item_watches)
        menu_item_watches.click()

        # Выбираем тип часов
        button_type_watch = driver.find_element(*self.locator_button_type_watch)
        button_type_watch.click()

        # Выбираем размер экрана часов
        button_watch_size = driver.find_element(*self.locator_button_watch_size)
        button_watch_size.click()

        # Листаем страницу и добавляем часы
        add_watch_to_cart = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(self.locator_add_watch_to_cart))
        driver.execute_script("window.scrollTo(0, 2300);")
        add_watch_to_cart.click()

        # Запоминаем название и цену часов для сравнения в корзине
        watch_name = driver.find_element(*self.locator_watch_name)
        self.watch_name_text = watch_name.text
        watch_price = driver.find_element(*self.locator_watch_price)
        watch_price_text = watch_price.text
        self.watch_price_to_int = int(watch_price_text.replace(" ", "").replace("₽", "").strip())

