import random
from time import sleep

from Element_position.my_home import My_home
from Element_position.base import Page
from selenium.webdriver.common.touch_actions import TouchActions


class my_home_operate(Page,My_home):

    def Click(self,n):
        """
        点击方法
        :return:
        """
        ss = self.find_element(*n)
        TouchActions(self.driver).tap(ss).perform()


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
        self.Click(self.toRedPond)

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
        self.Click(self.toRedPond_close)

    def Me(self):
        """
        点击我的
        :return:
        """
        # self.find_element(*self.me).click()
        self.wait_element_located(self.driver, self.me)
        self.Click(self.me)
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
        self.Click(self.login)

    def Setting(self):
        """
        点击系统设置
        :return:
        """
        self.wait_element_located(self.driver, self.setting)
        self.Click(self.setting)

    def Logout(self):
        """
        点击退出登录
        :return:
        """
        self.wait_element_located(self.driver, self.logout)
        self.Click(self.logout)

    def Register(self):
        """
        点击注册
        :return:
        """
        self.wait_element_located(self.driver,self.register)
        self.Click(self.register)

    def Register_phone(self):
        """
        注册输入手机号
        :return:
        """
        self.wait_element_located(self.driver, self.register_phone)
        self.find_element(*self.register_phone).send_keys(15500000001)

    def Register_auth_code(self):
        """
        注册输入验证码
        :return:
        """
        self.wait_element_located(self.driver, self.register_auth_code)
        self.find_element(*self.register_auth_code).send_keys(9527)

    def Register_password(self):
        """
        注册输入密码
        :return:
        """
        self.wait_element_located(self.driver, self.register_password)
        self.find_element(*self.register_password).send_keys(123456)

    def Register_bu(self):
        """
        点击立即注册
        :return:
        """
        self.wait_element_located(self.driver, self.register_bu)
        self.Click(self.register_bu)

    def Class_g(self):
        """
        点击分类
        :return:
        """
        self.wait_element_located(self.driver, self.class_g)
        self.Click(self.class_g)

    def goods_s(self):
        """
        点击二级分类
        :return:
        """
        self.wait_element_located(self.driver,self.goods)
        l=self.find_elements(*self.goods)
        print(len(l))
        if len(l)>1:
            i=random.randint(9,14)
            print(i)
            print(self.goods_n(i))
            self.wait_element_located(self.driver, self.goods_n(i))
            self.Click(self.goods_n(i))
            return 1
        else:
            print('无数据')
            return 0

    def good_all(self):
        """
        点击分类下的商品
        :return:
        """
        self.wait_element_located(self.driver, self.good_a)
        l = self.find_elements(*self.good_a)
        print(len(l))
        if len(l)>1:
            i = random.randint(1, 4)
            print(i)
            self.Click(self.good_a_n(i))
            return 1
        else:
            print('无数据')
            return 0