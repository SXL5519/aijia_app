from selenium.webdriver.common.by import By
####  我的页面元素定位
class My_home():
    aijia_t=(By.ID,"com.tencent.mm:id/zq")###w   艾家公社体验版
    toRedPond=(By.CLASS_NAME,'android.widget.Image')###点击首页弹框
    toRedPond_close= (By.CLASS_NAME, 'android.widget.Image')  ###首页弹框关闭
    # me=(By.ID,'com.tencent.mm:id/cv')##点击我的
    me = (By.NAME,'我的')  ##点击我的
    phone=(By.XPATH,"//android.view.View[@text='请输入您的手机号']")
    password=(By.XPATH,"//android.view.View[@text='请输入您的登录密码']")
    login=(By.XPATH,"//android.view.View[@text='/n立即登录']")
    # login = (By.NAME, "立即登录")
    setting=(By.XPATH,"//android.view.View[@text='系统设置']")
    logout=(By.XPATH,"//android.view.View[@text='退出登录']")