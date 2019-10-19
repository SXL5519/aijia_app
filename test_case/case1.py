from test_case.mytest import MyTest
from Array_Elements.My_home_operate import my_home_operate
from time import sleep

def logout(func):
    def wrapper(self,*args,**kwargs,):
        r=func(self,*args,**kwargs)
        hb = my_home_operate(self.driver)
        hb.Me()
        hb.swipeUp()
        hb.Setting()
        hb.Logout()
        return r
    return wrapper


class My_home_case(MyTest):

    def test_ToRedPond_case(self):
        '''点击首页弹框'''
        ha=my_home_operate(self.driver)
        ha.swipeDown()
        a=ha.aijia_c()
        # ha.cekout_switch(a[1])
        ha.ToRedPond()

    @logout
    def test_me_case(self):
        '''登录'''
        ha=my_home_operate(self.driver)
        ha.swipeDown()
        a=ha.aijia_c()
        ha.ToRedPond_close()
        # ha.click_tap([[468,1344],[612,1491]])
        ha.Me()
        ha.send_phone()
        ha.send_password()
        ha.click_tap([[208,1072],[1072,1092]])
