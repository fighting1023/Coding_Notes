# coding:utf-8
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import warnings

warnings.filterwarnings('ignore')


def sleep_sed_num():
    """设置随机睡眠时间"""
    sed = random.uniform(2, 3)
    time.sleep(sed)


def login():
    """登录操作"""
    username = 'xxx'
    password = 'xxx'

    print('用户登录...')
    opt = webdriver.ChromeOptions()  # 创建浏览器
    print('\t' + "浏览器已打开")
    driver = webdriver.Chrome(options=opt)
    driver.get('http://xxx.xxx.xxx.xxx/user/login')  # 打开目标网址
    print('\t' + "登录网页已打开")
    driver.maximize_window()  # 窗口最大化
    sleep_sed_num()  # 停留几秒
    inputs = driver.find_elements_by_tag_name("input")
    for input_ in inputs:
        if input_.get_attribute("type") == "text":
            input_.send_keys(username)
            print('\t' + '用户名已输入')
            sleep_sed_num()
        if input_.get_attribute("type") == "password":
            input_.send_keys(password)
            print('\t' + '密码已输入')
    print('\t' + '请在 10 秒内输入验证码！')
    time.sleep(10)
    ele_btn_login = driver.find_element_by_class_name("login_btn")
    ele_btn_login.click()
    sleep_sed_num()
    print('\t' + '您已登录\n\n')
    return driver


def play_video(driver, website, count_courses):
    """播放视频"""
    driver.get(website)
    sleep_sed_num()
    # 获取课程的名称
    course_name = driver.find_element_by_xpath('//div[@class="video_cont"]//h2').text
    print('课程名称:', course_name)

    for i in range(1, count_courses + 1):
        # 判断视频是否播放完成，同时获取视频的链接
        a = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/ul/li[%d]/a' % i)  # 定位到a标签
        href = a.get_attribute('href')  # 获取a标签下的视频链接，即href属性值
        style = a.get_attribute('style')  # 获取a标签下的style属性值，用于判断视频是否播放完成
        video_name = a.text  # 获取a标签下的文本值，即当前视频的名称

        course_time_span = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[4]/ul/li[%d]/span' % i).text  # 获取视频长度

        print('\t视频名称:', '%d/%d' % (i, count_courses), video_name)

        course_end_time = int(time.time()) + 3600 * int(course_time_span[0:2]) + 60 * int(course_time_span[3:5]) + int(
            course_time_span[6:8]) + 30  # 在视频长度的基础上延长30秒，即使视频的强制结束时间

        if 'red' in style:  # 判断视频是否播放完成，规则：视频名称是否变红色
            print('\t\t视频已完成\n')
            continue
        print('\t  预计播放时间：', jitime.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))), ' ==> ',
              time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(course_end_time)))
        driver.get(href)

        # 弹窗检测 超过结束时间后强制结束当前视频
        count_continue = 0
        while True:
            if time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(course_end_time)) \
                    < time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))):
                print('\t\t视频已完成')
                break
            time.sleep(1)
            try:
                WebDriverWait(driver, 2, 0.5).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "public_submit")))
                time.sleep(1)
                driver.find_element_by_class_name('public_submit').click()
                count_continue += 1
                print('\t\t已关闭【继续】弹窗次数：', count_continue, '\t',
                      time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))
                time.sleep(5)
            except:
                pass


websites = [
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3510&r=video&t=2', 8],  # [课程1链接，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3518&r=video&t=2', 7],  # [课程2，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3526&r=video&t=2', 16],  # [课程3，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3528&r=video&t=2', 4],  # [课程4，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3555&r=video&t=2', 6],  # [课程5，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3563&r=video&t=2', 4],  # [课程6，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3568&r=video&t=2', 2],  # [课程7，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3601&r=video&t=2', 4],  # [课程8，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3608&r=video&t=2', 5],  # [课程9，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3508&r=video&t=2', 8],  # [课程10，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3509&r=video&t=2', 20],  # [课程11，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3512&r=video&t=2', 11],  # [课程12，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3544&r=video&t=2', 12],  # [课程13，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3564&r=video&t=2', 3],  # [课程14，视频个数]
    ['http://xxx.xxx.xxx.xxx/fzdx/play?v_id=3579&r=video&t=2', 2],  # [课程15，视频个数]
]
if __name__ == '__main__':
    driver = login()
    for i in range(len(websites)):
        play_video(driver, websites[i][0], websites[i][1])