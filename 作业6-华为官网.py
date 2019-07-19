'''
登录华为官网 https://www.vmall.com/，
点击 "华为官网" 链接

检查 "华为官网" 页面上是否 有如下主菜单

  智能手机
  笔记本
  平板
  穿戴设备
  智能家居
  更多产品
  软件应用
  服务与支持



最后再回到主窗口， 检查鼠标停留在 "笔记本&平板" 处的时候， 是否显示的菜单有
"平板电脑  笔记本电脑 笔记本配件"

怎么模拟鼠标停留事件，请大家自行网上搜索，看看能不能自己解决问题。
'''
from selenium import webdriver
driver=webdriver.Chrome(r'F:\webdriver\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(10)
driver.get(r'https://www.vmall.com/')
# 找到“华为官网”点击
driver.find_element_by_css_selector("a[href='http://consumer.huawei.com/cn/']").click()
str1='智能手机|笔记本|平板|智能穿戴|智能家居|更多产品|软件应用|服务与支持'
# 鼠标悬停
from selenium.webdriver.common.action_chains import ActionChains
ac1=ActionChains(driver)
ac1.move_to_element(driver.find_element_by_css_selector('div.s-sub>ul>li:nth-last-child(1)')).perform()
# 找到“更多精彩”下边的应用市场,点击
driver.find_element_by_css_selector('div.dropdown-more a[href="http://appstore.huawei.com/"]').click()
# 定义检查的函数，检查消费者页面
def checkHuawei():
    alist=[]
    lis=driver.find_elements_by_css_selector('div.left-box>ul>li')
    for li in lis:
        alist.append(li.text)
    titles1='|'.join(alist)
    if titles1==str1:
        print('“华为消费者业务官网”页面测试通过')
    else:
        print('“华为消费者业务官网”页面测试不通过！！！')

ac=ActionChains(driver)
str2='平板电脑|笔记本电脑|笔记本配件'
# 检查悬停的笔记本页面的检查
def checkVmall():
    list=[]
    # 移动鼠标
    ac.move_to_element(driver.find_element_by_id('zxnav_1')).perform()
    eles=driver.find_elements_by_css_selector('#zxnav_1 .subcate-item a span')
    for ele in eles:
        list.append(ele.text)
    checks='|'.join(list)
    if checks==str2:
        print('主页面笔记本电脑项测试通过')
    else:
        print('主页面笔记本电脑项测试不通过！！！')
# 遍历所有的handle进行切换
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "华为消费者业务官网" in driver.title:
        checkHuawei()
    elif "华为应用市场" in driver.title:
        print('该页面为“华为应用市场”')
    else:
        checkVmall()

driver.quit()




