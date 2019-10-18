from time import sleep

from Element_position.my_home import My_home
from Element_position.base import Page
from selenium.webdriver.common.touch_actions import TouchActions


class my_home_operate(Page,My_home):
    def aijia_c(self):
        """
        点击微信小程序（艾家公社体验版）
        :return:
        """
        self.find_element(*self.aijia_t).click()   ##点击艾家公社
        sleep(5)
        print(self.driver.contexts)
        return self.driver.contexts


    def ToRedPond(self):
        """
        点击首页弹框
        :return:
        """
        # self.find_element(*self.toRedPond).click()
        # self.find_element(*self.tocloseHBC).click()
        # js='wx.createSelectorQuery().select(".redPondImg").click();'
        # self.driver.execute_script(js)
        ss = self.find_element(*self.toRedPond)
        TouchActions(self.driver).tap(ss).perform()

    def Me(self):
        """
        点击我的
        :return:
        """
        # self.find_element(*self.me).click()
        s=self.find_element(*self.me)
        TouchActions(self.driver).tap(s).perform()
        print('点击成功')
        print(self.driver.contexts)


    def send_phone(self):
        """
        输入手机号
        :return:
        """
        self.find_element(*self.phone).send_keys(17602882784)


