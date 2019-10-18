from selenium.webdriver.common.by import By
####  我的页面元素定位
class My_home():
    aijia_t=(By.ID,"com.tencent.mm:id/zs")###w   艾家公社体验版
    toRedPond=(By.CLASS_NAME,'android.widget.Image')###点击首页弹框
    tocloseHBC = (By.CLASS_NAME, 'close-img')  ###关闭
    # me=(By.ID,'com.tencent.mm:id/cv')##点击我的
    me = (By.NAME,'我的')  ##点击我的
    phone=(By.CLASS_NAME,'phone-num')