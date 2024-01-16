from selenium.webdriver.common.by import By

class StartPageScooterLocators:
    #локатор в хедере
    ORDER_BUTTON_HEADER = (By.XPATH,  "//div/div[2]/button[text()='Заказать']")
    #локатор ниже на странице
    ORDER_BUTTON_FOOTER = (By.XPATH, "//div/div[5]/button[text()='Заказать']")

