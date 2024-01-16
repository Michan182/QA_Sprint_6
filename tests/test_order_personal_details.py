import pytest
from conftest import driver
from pages.page_object_create_order_methods import OrderKickscooter
from pages.qa_scooter_main_page import OrderMainPage
from pages.page_personal_details import OrderConfirmed
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestCreateOrder:
    @pytest.mark.parametrize("name,surname,adress",[
        ("Михаил","Михайлов","Ленинский проспект"),
        ("РР", "РР", "Улица Мира")
    ])
    def test_order_success_up_button(self, driver, name, surname, adress):
        """
        Первый позитивный тест на проверку создания заказа c валидными данными
        через кнопку создания заказа вверху экрана.
        Проверка по тексту Заказ оформлен.
        """
        order_scooter = OrderKickscooter(driver)
        order_scooter.go_to_site('https://qa-scooter.praktikum-services.ru')
        order_scooter_main_page = OrderMainPage(driver)
        order_scooter_main_page.click_on_order_button_header()#кликаем на кнопку заказать сверху
        order_scooter.set_name(name)
        order_scooter.set_surname(surname)
        order_scooter.set_adress(adress)
        order_scooter.set_metro_station()
        order_scooter.set_phone_number()
        order_scooter.click_proceed_button()
        order_scooter.set_rental_start_date()
        order_scooter.set_rental_time()
        order_scooter.click_finish_order_button()
        order_scooter.click_confirm_order_button()

        order_confirmation = OrderConfirmed(driver)
        elements = order_confirmation.get_elements_order_confirmed()
        assert any("Заказ оформлен" in element for element in elements)



    @pytest.mark.parametrize("name,surname,adress",[
        ("Джонни","Депп","Патриаршие Пруды"),
        ("ФФФ", "ФФФ", "Улица улиц")
    ])
    def test_order_success_down_button(self, driver, name, surname, adress):
        """
        Первый позитивный тест на проверку создания заказа c валидными данными
        через кнопку создания заказа внизу экрана.
        Проверка по тексту Заказ оформлен.
        """
        order_scooter = OrderKickscooter(driver)
        order_scooter.go_to_site('https://qa-scooter.praktikum-services.ru')
        order_scooter_main_page = OrderMainPage(driver)
        element = driver.find_element(By.XPATH, "//div/div[5]/button[text()='Заказать']")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div/div[5]/button[text()='Заказать']")))
        order_scooter_main_page.click_on_order_button_footer()  # кликаем на кнопку заказать снизу
        order_scooter.set_name(name)
        order_scooter.set_surname(surname)
        order_scooter.set_adress(adress)
        order_scooter.set_metro_station()
        order_scooter.set_phone_number()
        order_scooter.click_proceed_button()
        order_scooter.set_rental_start_date()
        order_scooter.set_rental_time()
        order_scooter.click_finish_order_button()
        order_scooter.click_confirm_order_button()

        order_confirmation = OrderConfirmed(driver)
        elements = order_confirmation.get_elements_order_confirmed()
        assert any("Заказ оформлен" in element for element in elements)
