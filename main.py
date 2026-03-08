from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from add_items import NewItem
from check_the_cart import CheckCart
from close_cart_item_window import CLoseWindow
from compare_items import CompareItems
from make_the_order import MakeOrder
from return_to_main_page import MainPage
from wishlist import MakeWishlist


# возможность добавлять дополнительные настройки для браузера
options = webdriver.ChromeOptions()
# опция, которая не позволит нашему браузеру закрыться
options.add_experimental_option("detach", True)
# заходим как гость, опция, которая отключает оповещения от Браузера, с просьбой смены пароля
options.add_argument("--guest")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
# расширение браузера на весь экран
driver.maximize_window()

base_url = 'https://pitergsm.ru/'
driver.get(base_url)

#Закрытие окна cookie
cookie_button = driver.find_element(By.XPATH, '//button[@id="cookie-consent-btn"]')
cookie_button.click()


"""Добавление товара через наведение мышки на список"""

print('Searching for new IPhone...')
new_iphone = NewItem()
new_iphone.add_iphone_to_cart(driver)
print('New IPhone added to cart!')

#закрываем окно с товаром после добавления его в корзину
close_cart_window = CLoseWindow()
close_cart_window.close_window(driver)

# Выход на главную страницу сайта
main_page = MainPage()
main_page.return_to_main_page(driver, base_url)


"""Добавление товара через клик в меню"""

print('Searching for new Watches...')
new_watch = NewItem()
new_watch.add_watch_to_cart(driver)
print('New Watches added to cart!')

#закрываем окно с товаром после добавления его в корзину
close_cart_window = CLoseWindow()
close_cart_window.close_window(driver)

# Выход на главную страницу сайта
main_page = MainPage()
main_page.return_to_main_page(driver, base_url)


"""Добавление товара в избранное"""

print('Making a wishlist...')
wishlist_item = MakeWishlist()
wishlist_item.make_wishlist(driver)
print('Now I have a wishlist!')

# Выход на главную страницу сайта
main_page = MainPage()
main_page.return_to_main_page(driver, base_url)


"""Сравнение товаров"""

print('Comparing items...')
compare_two_items = CompareItems()
compare_two_items.compare_items(driver)
print('Items compared!')


"""Переходим в корзину и сравниваем, что добавлено то, что мы хотели"""

checking_cart = CheckCart()
checking_cart.check_cart(driver, new_iphone.iphone_price_to_int, new_watch.watch_price_to_int, new_iphone.iphone_name_text, new_watch.watch_name_text)


"""Оформляем заказ (до итоговой кнопки оформить)"""

print('Filling the information...')
making_order = MakeOrder()
making_order.make_the_order(driver, new_iphone.iphone_price_to_int, new_watch.watch_price_to_int)
print('Ready to make an order!')
