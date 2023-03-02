import time
from base.PageFactory import PageFactory
from selenium.webdriver.common.keys import Keys

from utils.readProperties import ReadConfig


class CreateTopicPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.driver = driver
        self.timeout = 15
        self.highlight = True
        self.mobile_test = False
        self.strBackGround = ""
        self.strCurrentSit = ""
        self.strExpertNote = ""
        self.strCurrentSitGen = ""
        self.strExpertNoteGen = ""
        self.strBackGroundGen = ""

    locators = {
        "topicHeader": ('XPATH', '//body/div[@id="root"]/div[1]/main[1]/form[1]/h1[1]'),
        "createTopicBtn": ('XPATH', '//a[contains(text(),"New Topic")]'),
        "topictitle": ('XPATH', '//input[@id="topic-title"]'),
        "topicDescription": ('XPATH', '//input[@id="topic-description"]'),
        "activatioType": ('XPATH', '//select[@id="activation-type"]'),
        "topicSignal": ('XPATH', '//input[@id="topic-signal"]'),
        "subTopictitle": ('XPATH', '//input[@id="subtopic-title"]'),
        "subTopicdesc": ('XPATH', '//input[@id="subtopic-description"]'),
        "subTopiclabel": ('XPATH', '//input[@id="subtopic-label"]'),
        "subTopicdesc": ('XPATH', '//input[@id="subtopic-description"]'),
        "subTopicsignal": ('XPATH', '//input[@id="subtopic-signals"]'),
        "subTopicdesc": ('XPATH', '//input[@id="subtopic-description"]'),
        "saveandGenerate": (
            'XPATH', '//div[@class="css-zxkuec"]//button[@type="button"][normalize-space()="Save & Generate"]'),
        "currentSitutation": ('XPATH',
                              '//div[@data-testid="current-situation"]//button[@type="button"][normalize-space()="Generate Content"]'),
        "expertNotes": (
            'XPATH',
            '//div[@data-testid="expert-notes"]//button[@type="button"][normalize-space()="Generate Content"]'),
        "background": (
            'XPATH', '//div[@data-testid="background"]//button[@type="button"][normalize-space()="Generate Content"]'),
        "csTextBox": ('XPATH', '//body[1]/div[1]/div[1]/main[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[2]'),
        "expertTextBox": ('XPATH', '//body[1]/div[1]/div[1]/main[1]/form[1]/div[2]/div[4]/div[2]/div[1]/div[2]'),
        "backgroundTextBox": ('XPATH', '//body[1]/div[1]/div[1]/main[1]/form[1]/div[2]/div[5]/div[2]/div[1]/div[2]'),
        "sizeinput": ('CSS', '#size-input'),
        "SaveandGen": ('XPATH', '/html[1]/body[1]/div[3]/div[1]/div[3]/div[1]/section[1]/footer[1]/div[1]/button[2]'),
        "menuButton": ('CSS', '(//button[@id="menu-button-7"])[1]'),
        "clickOnMyTopic": ('CSS', '#menu-list-7-menuitem-3'),
        "searchTopic": ('CSS', 'input[aria-label="filter"]'),
        "currentSituationGen": ('CSS', 'div[data-testid="current-situation-prose"] p'),
        "ExpertNotesGen": ('CSS', 'div[data-testid="expert-notes-prose"] p'),
        "BackgroundGen": ('CSS', 'div[data-testid="background-prose"] p')

    }

    def createTopicTest(self, topic, dec, subTopicTitle, subTopicDec, SubTopicsignal):
        self.createTopicBtn.click_button()

        self.topicHeader.visibility_of_element_located()

        self.topictitle.set_text(topic)
        self.topicDescription.set_text(dec)

        time.sleep(5)
        self.subTopictitle.set_text(subTopicTitle)
        self.subTopicdesc.set_text(subTopicDec)
        self.subTopicsignal.set_text(SubTopicsignal)

        self.currentSitutation.click_button()
        self.expertNotes.click_button()
        self.background.click_button()

        time.sleep(5)

        self.strCurrentSit = self.csTextBox.get_text()

        self.expertTextBox.visibility_of_element_located()
        self.strExpertNote = self.expertTextBox.get_text()
        self.strBackGround = self.backgroundTextBox.get_text()
        print("---------------------")
        print(self.strCurrentSit)
        print("---------------------")
        self.saveandGenerate.click_button()
        self.sizeinput.visibility_of_element_located()
        time.sleep(5)
        self.sizeinput.clear_text()
        time.sleep(5)
        time.sleep(5)
        self.sizeinput.set_text(10)
        time.sleep(5)
        self.SaveandGen.click_button()
        time.sleep(15)
        self.driver.get(ReadConfig.getApplicationURL() + "/my-topics/")

        textbox_username_id = "//a[normalize-space()='" + topic + "']"

        element_field = self.driver.find_element("xpath", textbox_username_id)

        element_field.is_displayed()

        element_field.click()

        time.sleep(4)

        self.strBackGroundGen = self.BackgroundGen.get_text()
        self.strCurrentSitGen = self.currentSituationGen.get_text()
        self.strExpertNoteGen = self.ExpertNotesGen.get_text()
