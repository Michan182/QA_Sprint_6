from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderKickscooter(BasePage):
    #локатор поля Имя
    name_field = [By.CSS_SELECTOR, "input[placeholder='* Имя']"]
    # локатор поля Фамилия
    surname_field = [By.CSS_SELECTOR, "input[placeholder='* Фамилия']"]
    # локатор поля Адрес
    adress_field = [By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"]
    # локатор поля Станция Метро
    metro_station_field = [By.CSS_SELECTOR, "input[placeholder='* Станция метро']"]
    # локатор поля Телефон
    phone_number_filed = [By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]
    # локатор кнопки Далее
    proceed_button = [By.XPATH, '//button[text()="Далее"]']

    rental_start_date_field = [By.XPATH,'//input[@placeholder="* Когда привезти самокат"]']
    #локатор поля времени аренды самоката
    rental_time_field = [By.XPATH, "//div[text()='* Срок аренды']"]
    #локатор дропдауна выбора срока Сутки
    one_day_time = [By.XPATH, "//div[2]/div[2]/div[2]/div[2]/div[1]"]
    #локатор кнопки заказать после введения всех данных
    finish_order_button = [By.XPATH, "//div[3]/button[text()='Заказать']"]

    #локатор кнопки Подтвердить заказ
    confirm_order_button = [By.XPATH, '//button[text()="Да"]']
    #локатор кнопки Посмотреть статус
    check_status_button = [By.XPATH, '//button[text()="Посмотреть статус"]']

    #локатор лого "Самокат"
    samokat_logo = [By.XPATH, '//img[@alt="Scooter"]']

    #локатор лого "Яндекс"
    yandex_logo = [By.XPATH, '//img[@alt="Yandex"]']

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # метод вводит Имя
    def set_name(self, name):
        enter_name = self.driver.find_element(*self.name_field)
        enter_name.click()
        enter_name.send_keys(name)
        return enter_name

    # метод вводит Фамилию
    def set_surname(self, surname):
        enter_surname = self.driver.find_element(*self.surname_field)
        enter_surname.click()
        enter_surname.send_keys(surname)
        return enter_surname


    # метод вводит Адрес
    def set_adress(self, adress):
        enter_adress = self.driver.find_element(*self.adress_field)
        enter_adress.click()
        enter_adress.send_keys(adress)
        return enter_adress
    # метод вводит Станцию метро
    def set_metro_station(self):
        self.driver.find_element(*self.metro_station_field).click()
        self.driver.find_element(By.XPATH, "//div[text()='Черкизовская']").click()

    # метод вводит Телефон
    def set_phone_number(self):
        new_phone_number = "79118982345"
        self.driver.find_element(*self.phone_number_filed).send_keys(new_phone_number)
        return new_phone_number

    # метод кликает по кнопке Далее
    def click_proceed_button(self):
        self.driver.find_element(*self.proceed_button).click()
        return

    #метод выбирает дату доставки самоката
    def set_rental_start_date(self):
        self.driver.find_element(*self.rental_start_date_field).click()
        self.driver.find_element(By.XPATH, "//div[text()='30']").click() #выбираем 30 января

    #метод вводит кликает на дропдаун и выбирает срок аренды
    def set_rental_time(self):
        self.driver.find_element(*self.rental_time_field).click()
        self.driver.find_element(*self.one_day_time).click()

    def click_finish_order_button(self):
        self.driver.find_element(*self.finish_order_button).click()

    #метод кликает по кнопке Подтвердить заказ
    def click_confirm_order_button(self):
        self.driver.find_element(*self.confirm_order_button).click()
        return
    #метод кликает по кнопке Посмотреть статус
    def click_check_status_button(self):
        self.driver.find_element(*self.check_status_button).click()
        return
    #метод кликает по лого Самокат
    def click_samokat_logo(self):
        self.driver.find_element(*self.samokat_logo).click()
        return

    # метод кликает по лого Яндекс
    def click_yandex_logo(self):
        self.driver.find_element(*self.yandex_logo).click()
        return