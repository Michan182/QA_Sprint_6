from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class DropDownQuestions(BasePage):
    # локатор вопроса сколько стоит
    how_much = [By.XPATH, "//div[text()='Сколько это стоит? И как оплатить?']"]
    # локатор ответа на вопрос сколько стоит
    how_much_answer = [By.XPATH, "//*[@id='accordion__panel-16']/p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"]

    # локатор вопроса сколько самокатов можно заказать
    how_much_scooters = [By.XPATH, "//div[text()='Хочу сразу несколько самокатов! Так можно?']"]
    # локатор ответа на вопрос сколько самокатов можно заказать
    how_much_scooters_answer = [By.XPATH, "//div[@id='accordion__panel-1']/p"]

    # локатор вопроса сколько время аренды
    how_much_time = [By.XPATH, "//div[text()='Как рассчитывается время аренды?']"]
    # локатор ответа на вопрос сколько время аренды
    how_much_time_answer = [By.XPATH, "//div/p[text()='//*[@id='accordion__panel-18']/p/text()']"]

    # локатор вопроса сколько заказ сегодня
    order_today = [By.XPATH, "//div[text()='Можно ли заказать самокат прямо на сегодня?']"]
    # локатор ответа на вопрос заказ сегодня
    order_today_answer = [By.XPATH, "//*[@id='accordion__panel-19']/p"]

    # локатор вопроса можно ли продлить заказ
    order_extend_time = [By.XPATH, "//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"]
    # локатор ответа на вопрос можно ли продлить заказ
    order_extend_time_answer = [By.XPATH, "//*[@id='accordion__panel-20']/p/text()"]

    # локатор вопроса привозите ли зарядку
    charger_delivery = [By.XPATH, "//div[text()='Вы привозите зарядку вместе с самокатом?']"]
    # локатор ответа на вопрос привозите ли зарядку
    charger_delivery_answer = [By.XPATH, "//*[@id='accordion__panel-21']/p/text()"]

    # локатор вопроса можно ли отменить заказ
    cancel_order = [By.XPATH, "//div[text()='Можно ли отменить заказ?']"]
    # локатор ответа на вопрос можно ли отменить заказ
    cancel_order_answer = [By.XPATH, "//*[@id='accordion__panel-22']/p/text()"]

    # локатор вопроса можно ли привезти за МКАД
    far_delivery = [By.XPATH, "//div[text()='Я жизу за МКАДом, привезёте?']"]
    # локатор ответа на вопрос можно ли привезти за МКАД
    far_delivery_answer = [By.XPATH, "//*[@id='accordion__panel-23']/p/text()"]

    # метод инициализации класса
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # метод клика по вопросу сколько стоит
    def click_dropdown_button(self, locator):
        """
        Кликает по кнопке "Сколько это стоит? И как оплатить?"
        """
        # Ожидание, чтобы элемент появился на странице
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

        # Прокручиваем до элемента, чтобы он был виден на странице
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        # Ожидание, чтобы элемент стал кликабельным
        how_much = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

        how_much.click()

    def get_text_from_element(self, locator):
        return self.driver.find_element(By.XPATH, locator).text
