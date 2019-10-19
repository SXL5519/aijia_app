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
        self.wait_element_located(self.driver,self.aijia_t)
        self.find_element(*self.aijia_t).click()   ##点击艾家公社
        # print(self.driver.contexts)
        # return self.driver.contexts


    def ToRedPond(self):
        """
        点击首页弹框
        :return:
        """
        # self.find_element(*self.toRedPond).click()
        # self.find_element(*self.tocloseHBC).click()
        # js='wx.createSelectorQuery().select(".redPondImg").click();'
        # self.driver.execute_script(js)
        self.wait_element_located(self.driver, self.toRedPond)
        ss = self.find_element(*self.toRedPond)
        TouchActions(self.driver).tap(ss).perform()

    def ToRedPond_close(self):
        """
        点击取消首页弹框
        :return:
        """
        # self.find_element(*self.toRedPond).click()
        # self.find_element(*self.tocloseHBC).click()
        # js='wx.createSelectorQuery().select(".redPondImg").click();'
        # self.driver.execute_script(js)
        self.wait_element_located(self.driver, self.toRedPond_close)
        ss = self.find_element(*self.toRedPond_close)
        TouchActions(self.driver).tap(ss).perform()

    def Me(self):
        """
        点击我的
        :return:
        """
        # self.find_element(*self.me).click()
        self.wait_element_located(self.driver, self.me)
        s=self.find_element(*self.me)
        TouchActions(self.driver).tap(s).perform()
        print('点击成功')
        print(self.driver.contexts)


    def send_phone(self):
        """
        输入手机号
        :return:
        """
        # self.find_element(*self.phone).click()
        self.wait_element_located(self.driver,self.phone)
        self.find_element(*self.phone).send_keys(17602882784)

    def send_password(self):
        """
        输入密码
        :return:
        """
        self.wait_element_located(self.driver, self.password)
        self.find_element(*self.password).send_keys('159369sxl')

    def Login(self):
        """
        点击登录按钮
        :return:
        """
        self.wait_element_located(self.driver, self.login)
        q=self.find_element(*self.login)
        TouchActions(self.driver).tap(q).perform()

    def Setting(self):
        """
        点击系统设置
        :return:
        """
        self.wait_element_located(self.driver, self.setting)
        q = self.find_element(*self.setting)
        TouchActions(self.driver).tap(q).perform()

    def Logout(self):
        """
        点击退出登录
        :return:
        """
        self.wait_element_located(self.driver, self.logout)
        q = self.find_element(*self.logout)
        TouchActions(self.driver).tap(q).perform()