from selenium.webdriver.common.by import By
from Pages.BasePage import UiObject


class RechargePage:
    operator=UiObject(By.XPATH, "//input[@data-qa='celular-operator']")
    telcel=UiObject(By.XPATH, "//li[@data-show='Telcel']")
    mobileno=UiObject(By.XPATH, "//input[@data-qa='celular-mobile']")
    amount=UiObject(By.XPATH, "//input[@data-qa='celular-amount']")
    recharge=UiObject(By.XPATH, "//a[div[text()='Recarga $10']]")
    celular_pay=UiObject(By.XPATH, "//button[@data-qa='celular-pay']")

    def enter_recharge_value(self,mobile_no)->bool:
        self.operator.click()
        self.telcel.click()
        self.mobileno.set_text(mobile_no)
        self.amount.click()
        self.recharge.click()
        self.celular_pay.click()
        return True
