import allure
import pytest

from pages.page_object_dropdown import DropDownQuestions

@allure.story('tests')
class TestDropdown:
    @allure.title('test questions')
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text",
                             [(DropDownQuestions.how_much, DropDownQuestions.how_much_answer,
                               "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
                              (DropDownQuestions.how_much_scooters, DropDownQuestions.how_much_scooters_answer,
                               "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, "
                               "можете просто сделать несколько заказов — один за другим."),
                              (DropDownQuestions.how_much_time, DropDownQuestions.how_much_time_answer,
                               "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт " \
                               "времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли " \
                               "самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
                              (DropDownQuestions.order_today, DropDownQuestions.order_today_answer,
                               "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
                              (DropDownQuestions.order_extend_time, DropDownQuestions.order_extend_time_answer,
                               "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
                              (DropDownQuestions.charger_delivery, DropDownQuestions.charger_delivery_answer,
                               "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете " \
                               "кататься без передышек и во сне. Зарядка не понадобится."),
                              (DropDownQuestions.cancel_order, DropDownQuestions.cancel_order_answer,
                               "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все " \
                               "же свои."),
                              (DropDownQuestions.far_delivery, DropDownQuestions.far_delivery_answer,
                               "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
                              ])
    def test_dropdown_questions(self, driver, question_locator, answer_locator, expected_text):
        """
        Параметризованный тест проверки раскрытия dropdown в разделе "Вопросы" на первые два вопроса:.
        Сколько стоит?
        Сколько можно заказать самокатов?
        """
        dropdown = DropDownQuestions(driver)
        dropdown.go_to_site('https://qa-scooter.praktikum-services.ru')
        dropdown.scroll_and_click_element(question_locator)
        dropdown.find_element_located(answer_locator)
        element = dropdown.get_text_from_element(answer_locator)
        assert element == expected_text

