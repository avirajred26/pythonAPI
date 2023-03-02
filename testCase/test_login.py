from pageObject.LoginPage import LoginPage
from pageObject.CluePagePage import CluePage
from utils.readProperties import ReadConfig
from utils.customLogger import LogGen


class Test_Login_001:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_login12(self, setup):
        self.logger.info("*************** " + self.__class__.__name__ + " *****************")
        self.driver = setup
        self.logger.info("*************** Browser is opneing *****************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.login(self.username,self.password)

        if self.lp.checkButtonBol != True:
            self.logger.info("****Login test failed ****")
        else:
            self.logger.info("****Login test passed ****")

        self.cp = CluePage(self.driver)
        self.cp.clueSearch("Litigation Financing")






