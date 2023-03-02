from selenium.common import NoSuchElementException

from pageObject.CreateTopic import CreateTopicPage
from pageObject.LoginPage import LoginPage

from utils.readProperties import ReadConfig
from utils.customLogger import LogGen


class Test_CreateTopic_002:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_CreateTopic(self, setup):

        self.logger.info("*************** "+self.__class__.__name__+" *****************")
        self.driver = setup
        self.logger.info("*************** Browser is opening *****************")
        self.driver.maximize_window()
        self.driver.get(self.baseURL+"/login/")
        self.lp = LoginPage(self.driver)
        self.lp.login(self.username, self.password)

        try:
            assert self.lp.verifyHomeElement.is_element_present()
            self.logger.info("****Login test passed ****")
        except NoSuchElementException as e:
            self.logger.info("****Login test failed ****")

        self.cp = CreateTopicPage(self.driver)
        self.cp.createTopicTest("Selenium To be tested1234567", "Selenium1", "Selenium Testing", "Selenium Testing", "crude Oil")
        print(self.cp.strCurrentSit)
        try:
            assert self.cp.strExpertNoteGen == self.cp.strExpertNote
            assert self.cp.strCurrentSitGen == self.cp.strCurrentSit
            assert self.cp.strExpertNoteGen == self.cp.strExpertNote
            self.logger.info("**** Create topic test  passed ****")
        except NoSuchElementException as e:
            self.logger.info("****Create topic test failed ****")

