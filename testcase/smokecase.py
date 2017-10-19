#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import report
class login(unittest.TestCase):
    def setUp(self):
        self.open = webdriver.Chrome()
        time.sleep(1)
    def tesarDown(self):
        self.open.quit()
    def test_login(self):
        self.open.get("https://www.baidu.com/")
        self.open.find_element_by_id("kw").send_keys("saber")
        time.sleep(2)
if __name__ == '__main__':
    unittest.main()
# unittest.main()    运行，加载不用加
