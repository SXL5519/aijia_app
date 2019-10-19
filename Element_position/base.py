
class Page():

    base_url="http://117.185.7.60:35180/#/?VNK=21688764"

    #初始化方法
    def __init__(self,driver,url=base_url):
        self.driver = driver
        self.url = url
        self.time=30

    #打开相应网址
    def open(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.time)

    #二次封装元素定位的方法
    def find_element(self,*loc):

        return self.driver.find_element(*loc)

    def find_elements(self, *loc):

        return self.driver.find_elements(*loc)

    def swipeDown(self,t=500,n=1):
        """
        在微信首页下拉屏幕
        :return:
        """
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeUp(self,t=500,n=1):
        """
        在微信首页下拉屏幕
        :return:
        """
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def cekout_switch(self,n):
        """
        切换原生或者webviwe
        :return:
        """
        self.driver.switch_to.context(n)
        print('切换成功：%s'%n)

    def click_tap(self,n):
        """
        根据坐标点击
        :return:
        """
        X = self.driver.get_window_size()['width']
        Y = self.driver.get_window_size()['height']
        n[0][0]=n[0][0]/1080*X
        n[0][1] = n[0][1] / 1080 * X
        n[1][0]=n[1][0]/1920*Y
        n[1][1] = n[1][1] / 1920 * Y
        self.driver.tap(n,500)
        print('点击成功')