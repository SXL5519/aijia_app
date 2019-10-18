from test_case.mytest import MyTest
from Array_Elements.My_home_operate import my_home_operate
from time import sleep

class My_home_case(MyTest):
    def test_me_case(self):
        '''打开艾家公社小程序'''
        ha=my_home_operate(self.driver)
        ha.swipeDown()
        sleep(10)
        a=ha.aijia_c()
        # ha.cekout_switch(a[1])
        sleep(50)
        ha.ToRedPond()
        # ha.click_t()
        # ha.cekout_switch(a[0])
        sleep(15)
        # ha.Me()
        # sleep(15)
        # ha.cekout_switch(a[1])
        # sleep(10)
        # ha.send_phone()
        # sleep(20)

