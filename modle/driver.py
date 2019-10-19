#from selenium import webdriver
from appium import webdriver
from time import sleep

class Chrome():
     def connect(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'

        desired_caps['platformVersion'] = '8.1.0'  # oppo r15
        desired_caps['deviceName'] = 'W4GUJFPZV8CY55WC'   #设备编码
        desired_caps['appPackage'] = 'com.tencent.mm'  #app包名
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}
        # desired_caps['appWaitActivity'] = 'com.hxwj.wkj/com.hxwj.wkj.act.ActMain'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(2)
        #   driver.find_element_by_name("1").click()
        sleep(1)
        return self.driver


'''class Chrome():
    # 配置谷歌浏览器模拟'Galaxy S5'手机打开浏览器
    mobileEmulation = {'deviceName': 'Galaxy S5'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    #驱动最大化打开谷歌浏览器
    def browser_chrome(self):
        self.driver=webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\\chromedriver.exe',
                                     chrome_options=self.options)

        self.driver.maximize_window()

        return self.driver'''