from pages.page_object_dropdown import DropDownQuestions
from selenium.webdriver.common.by import By
import pytest
from conftest import driver

class TestDropdown:
    def test_dropdown_how_much(self, driver):
        """
        Данный тест проверяет раскрытие dropdown сколько стоит
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.click_dropdown_button(DropDownQuestions.how_much)
        #находим текст в раскрытом дропдауне
        element1 = driver.find_element(By.XPATH, "//div[@id='accordion__panel-0']/p").text
        # Получить текст между тегами <p>
        text_inside = element1
        # ожидаемый текст
        expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_how_much_scooters(self, driver):
        """
        Данный тест проверяет раскрытие dropdown сколько можно заказать самокатов
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.click_dropdown_button(DropDownQuestions.how_much_scooters)
        # находим текст в раскрытом дропдауне
        element1 = driver.find_element(By.XPATH, "//div[@id='accordion__panel-1']/p").text
        # Получить текст между тегами <p>
        text_inside = element1
        # ожидаемый текст
        expected_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        # текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_how_much_time(self, driver):
        """
        Данный тест проверяет раскрытие dropdown сколько стоит
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.click_dropdown_button(DropDownQuestions.how_much_time)
        #находим текст в раскрытом дропдауне
        element1 = driver.find_element(By.XPATH, "//div[@id='accordion__panel-2']/p").text
        # Получить текст между тегами <p>
        text_inside = element1
        # ожидаемый текст
        expected_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт " \
                        "времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли " \
                        "самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_order_taday(self, driver):
        """
        Данный тест проверяет раскрытие dropdown сколько стоит
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.click_dropdown_button(DropDownQuestions.order_today)
        #находим текст в раскрытом дропдауне
        element1 = driver.find_element(By.XPATH, "//div[@id='accordion__panel-3']/p").text
        # Получить текст между тегами <p>
        text_inside = element1
        # ожидаемый текст
        expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_order_extend_time(self, driver):
        """
        Данный тест проверяет раскрытие dropdown сколько стоит
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.click_dropdown_button(DropDownQuestions.order_extend_time)
        #находим текст в раскрытом дропдауне
        element1 = driver.find_element(By.XPATH, "//div[@id='accordion__panel-4']/p").text
        # Получить текст между тегами <p>
        text_inside = element1
        # ожидаемый текст
        expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_charger_delivery(self, driver):
        """
        Данный тест проверяет раскрытие dropdown сколько стоит
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.click_dropdown_button(DropDownQuestions.charger_delivery)
        #находим текст в раскрытом дропдауне
        element1 = driver.find_element(By.XPATH, "//div[@id='accordion__panel-5']/p").text
        # Получить текст между тегами <p>
        text_inside = element1
        # ожидаемый текст
        expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете " \
                        "кататься без передышек и во сне. Зарядка не понадобится."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_cancel_order(self, driver):
        """
        Данный тест проверяет раскрытие dropdown сколько стоит
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.click_dropdown_button(DropDownQuestions.cancel_order)
        #находим текст в раскрытом дропдауне
        element1 = driver.find_element(By.XPATH, "//div[@id='accordion__panel-6']/p").text
        # Получить текст между тегами <p>
        text_inside = element1
        # ожидаемый текст
        expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все " \
                        "же свои."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text

    def test_dropdown_far_delivery(self, driver):
        """
        Данный тест проверяет раскрытие dropdown сколько стоит
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.click_dropdown_button(DropDownQuestions.far_delivery)
        #находим текст в раскрытом дропдауне
        element1 = driver.find_element(By.XPATH, "//div[@id='accordion__panel-7']/p").text
        # Получить текст между тегами <p>
        text_inside = element1
        # ожидаемый текст
        expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        #текст совпадает с ожидаемым
        assert text_inside == expected_text