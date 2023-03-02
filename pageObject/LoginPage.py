from base.PageFactory import PageFactory


class LoginPage(PageFactory):
    checkButtonBol = True

    def __init__(self, driver):
        self.driver = driver
        self.driver = driver
        self.timeout = 15
        self.highlight = True
        self.mobile_test = False

    locators = {
        "edtUserName": ('ID', 'username'),
        "edtPassword": ('ID', 'password'),
        "btnSignIn": ('XPATH', '//button[contains(text(),"Sign In")]'),
        "verifyHomeElement": ('XPATH', '//body/div[@id="root"]/div[1]/main[1]/div[1]/div[1]/h1[1]/img[1]')

    }

    def login(self, username, password):
        # set_text(), click_button() methods are extended methods in PageFactory
        self.edtUserName.set_text(username)  # edtUserName become class variable using PageFactory
        self.edtPassword.set_text(password)
        self.checkButtonBol = self.btnSignIn.element_to_be_clickable()
        print(self.checkButtonBol)
        self.btnSignIn.click_button()
