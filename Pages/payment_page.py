from selenium.webdriver.common.by import By

from BrowserManager import Browser
from Pages.BasePage import UiObject
from time import sleep

class PaymentPage:
    header=UiObject(By.XPATH, "//div[text()='Resumen de la compra']")
    tarjeta=UiObject(By.XPATH,"//p[text()='Tarjeta']")
    usar_nueva_radio=UiObject(By.XPATH,"//span[text()='Usar nueva tarjeta']")
    card_no=UiObject(By.XPATH,"//input[@id='cardnumberunique']")
    exp_month=UiObject(By.XPATH,"//input[@data-qa='mes-input']")
    exp_year=UiObject(By.XPATH,"//input[@data-qa='expyear-input']")
    ccv=UiObject(By.XPATH,"//input[@data-qa='cvv-input']")
    email=UiObject(By.XPATH,"(//input[@name='txtEmail'])[1]")
    payment=UiObject(By.XPATH,"//button[contains(@class,'Payment')]//span[text()='Pagar con Tarjeta']")
    popup_email=UiObject(By.XPATH,"//input[@id='usrname']")
    popup_password=UiObject(By.XPATH,"//input[@id='psw']")
    captcha=UiObject(By.XPATH,"//span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox']")
    popup_login_button=UiObject(By.XPATH,"//button[@name='loginbtn']")
    popup_message=UiObject(By.XPATH,"//p[@class='message']")
    success_message=UiObject(By.XPATH,"//div[text()='Ya estás logueado, ahora puedes hacer tu pago.']")
    frames=UiObject(By.XPATH,"(//iframe[@title='reCAPTCHA'])[1]")
    def fill_payment(self,cardno,expmonth,expyear,ccv,email)->bool:
        self.tarjeta.click()
        sleep(2)
        self.usar_nueva_radio.click()
        sleep(2)
        self.card_no.set_text(cardno)
        self.exp_month.set_text(expmonth)
        self.exp_year.set_text(expyear)
        self.ccv.set_text(ccv)
        self.email.set_text(email)
        self.payment.click()
        return True
    def fill_popup(self,email,password)->bool:
        sleep(10)
        self.popup_email.set_text(email)
        self.popup_password.set_text(password)
        sleep(4)
        Browser.get_driver().switch_to_frame(0)
        self.captcha.click()
        Browser.get_driver().switch_to.default_content()
        #Browser.get_driver().switch_to_window(Browser.get_driver().window_handles[0])
        self.popup_login_button.click()
        return True



