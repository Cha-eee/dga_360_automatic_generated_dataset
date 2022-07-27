from selenium import webdriver
import time
import os
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import pyperclip
import shutil
import traceback
import datetime

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': 'D:/Projects/'}
options.add_experimental_option('prefs', prefs)
# dga.txt下载到downloads中
driver = webdriver.Chrome()
url = "https://data.netlab.360.com/dga/"
wait = ui.WebDriverWait(driver, 10)
driver.get(url)
element = driver.find_element_by_xpath("//a[@href='/feeds/dga/dga.txt']")
action = ActionChains(driver).move_to_element(element)
action.context_click(element).perform()
pyautogui.typewrite(['k'])
time.sleep(1)
pyautogui.typewrite(['enter'])
time.sleep(60)
driver.quit()


# 移动文件
def move_file(src_path, dst_path, file):
    print
    'from : ', src_path
    print
    'to : ', dst_path
    try:
        # cmd = 'chmod -R +x ' + src_path
        # os.popen(cmd)
        f_src = os.path.join(src_path, file)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        f_dst = os.path.join(dst_path, file)
        shutil.move(f_src, f_dst)
    except Exception as e:
        print
        'move_file ERROR: ', e
        traceback.print_exc()


yesterday = datetime.datetime.now() + datetime.timedelta(-1)
date = yesterday.strftime('%x')
date= date.replace('/', '-')
path = 'D:/Projects/'
name = str(path) + 'dga.txt'
new_name = str(path) + 'dga' + str(date) + '.txt'
if os.path.exists(name):
    os.rename(name, new_name)

move_file('C:/Users/Downloads/', path, 'dga.txt')

os.system('python D:/Projects/txttocsv.py')
