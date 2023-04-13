import time

from selenium import webdriver


# 输入大麦网的登录信息
username = '13710942992'
password = '98106515cheng!'

# 输入要抢票的演出的 URL
url = 'https://www.damai.cn/'

# 初始化 WebDriver
driver = webdriver.Chrome()
driver.get(url)

# 登录大麦网
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul/li[2]/a').click()
time.sleep(1)
driver.find_element_by_id('login_email').send_keys(username)
driver.find_element_by_id('login_pwd_txt').send_keys(password)
driver.find_element_by_xpath('/html/body/div[14]/div[2]/div[3]/div/div/div/div[2]/form/ul/li[6]/input').click()

# 进入演出页面
driver.get(url)
time.sleep(1)

# 抢票
while True:
    try:
        # 在这里编写抢票的代码bi
        break
    except:
        time.sleep(0.1)

# 关闭 WebDriver
driver.quit()
