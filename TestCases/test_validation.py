import pytest
from selenium.webdriver.common.by import By

from BrowserManager import Browser
from Pages.BasePage import UiObject
from time import sleep

from Pages.payment_page import PaymentPage
from Pages.recharge_cellular_page import RechargePage


class TestValidation:

    def test_case1(self):
        Browser.create_new_driver(Browser.CHROME)
        Browser.get_driver().maximize_window()
        Browser.get_driver().get('http://sanbox.undostres.com.mx')
        recharge_page=RechargePage()
        assert recharge_page.enter_recharge_value(mobile_no='8465433546'),'Recharge pay value not selected'
        #secondpage
        UiObject(By.XPATH,"//div[text()='Resumen de la compra']").exists()
        payment_page=PaymentPage()
        assert payment_page.fill_payment('4111111111111111','11','25','111','test@test.com'),'paymentpage data not entered/working'
        assert payment_page.fill_popup('automationexcersise@test.com','123456'),'not able to login'
        assert payment_page.success_message.get_text()=='Ya estás logueado, ahora puedes hacer tu pago.','success message not displaying'
        Browser.shutdown()
