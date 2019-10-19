from selenium.webdriver.common.by import By
####  我的页面元素定位
class My_home():
    aijia_t=(By.ID,"com.tencent.mm:id/zq")###w   艾家公社体验版
    toRedPond=(By.CLASS_NAME,'android.widget.Image')###点击首页弹框
    toRedPond_close= (By.XPATH, "//android.view.View/android.view.View[2]/android.view.View[1]/android.widget.Image[1]")  ###首页弹框关闭
    # me=(By.ID,'com.tencent.mm:id/cv')##点击我的
    me = (By.NAME,'我的')  ##点击我的
    phone=(By.XPATH,"//android.view.View[@text='请输入您的手机号']")
    password=(By.XPATH,"//android.view.View[@text='请输入您的登录密码']")
    login=(By.XPATH,"//android.view.View[@text='/n立即登录']")
    # login = (By.NAME, "立即登录")
    setting=(By.XPATH,"//android.view.View[@text='系统设置']")
    logout=(By.XPATH,"//android.view.View[@text='退出登录']")
    register=(By.XPATH,"//android.view.View[@text='快速注册']")
    register_phone=(By.XPATH,"//android.view.View[@text='请输入您的手机号']")
    register_auth_code=(By.XPATH,"//android.view.View[@text='请输入您的验证码']")
    register_password=(By.XPATH,"//android.view.View[@text='请输入您的登录密码']")
    register_bu=(By.CLASS_NAME,"android.widget.Button")###立即注册
    class_g=(By.XPATH,"//android.widget.TextView[@text='分类']")
    goods=(By.CLASS_NAME,"android.widget.Image")###所有二级分类图片
    def goods_n(self,n):
        good_i=(By.XPATH,"//android.webkit.WebView[@text='wx1ed73850b7173563:pages/main/class/class.html:VISIBLE']/android.widget.Image[%d]"%n)
        return good_i

    good_a=(By.CLASS_NAME,"android.widget.Image")##当前分类下的所有商品图片

    def good_a_n(self,n):
        good_n=(By.XPATH,"//android.view.View/android.view.View[4]/android.widget.Image[%d]"%n)
        return good_n