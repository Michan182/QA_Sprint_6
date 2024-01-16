from conftest import driver
from pages.page_object_create_order_methods import OrderKickscooter
from pages.qa_scooter_main_page import OrderMainPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestReturnToMainPage:
    def test_return_to_main_page_by_samokat_logo(self, driver):
        """
        Тест проверяет: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
        """
        order_scooter = OrderKickscooter(driver)
        order_scooter.go_to_site('https://qa-scooter.praktikum-services.ru')
        order_scooter_main_page = OrderMainPage(driver)
        order_scooter_main_page.click_on_order_button_header()#кликаем на кнопку заказать сверху
        order_scooter.click_samokat_logo()

        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    def test_return_to_main_page_by_yandex_logo(self, driver):
        """
        Тест проверяет: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.
        """
        order_scooter = OrderKickscooter(driver)
        order_scooter.go_to_site('https://qa-scooter.praktikum-services.ru')
        order_scooter_main_page = OrderMainPage(driver)
        order_scooter_main_page.click_on_order_button_header()  # кликаем на кнопку заказать сверху

        # Получаем текущее окно (вкладку)
        current_window = driver.current_window_handle

        # Переходим на новую вкладку (кликаем по логотипу Яндекса)
        order_scooter.click_yandex_logo()

        # Ждем, пока появится новая вкладка (окно)
        WebDriverWait(driver, 10).until(expected_conditions.number_of_windows_to_be(2))

        # Получаем список всех вкладок (окон)
        all_windows = driver.window_handles

        # Находим ID новой вкладки
        new_window = [window for window in all_windows if window != current_window][0]

        # Переключаемся на новую вкладку
        driver.switch_to.window(new_window)

        # Ждем, пока браузер не переключится на новую вкладку
        WebDriverWait(driver, 10).until(expected_conditions.url_contains("https://dzen.ru/"))

        # Проверяем, что URL на новой вкладке содержит "https://dzen.ru/"
        expected_url_part = "https://dzen.ru/"
        assert expected_url_part in driver.current_url, f"Ожидаемый URL должен содержать {expected_url_part}, Фактический URL: {driver.current_url}"
