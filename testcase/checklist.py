#coding=utf-8
import unittest
from ecshop.public import ITLEOFramework

class itleo(unittest.TestCase):
    def setUp(self):     #函数的self
        self.br=ITLEOFramework.ITleoFramework('chrome')
    def teaeDown(self):
        br = self.br
        br.quit()
        pass

    def test_login(self):
        """验证ecshop异常登录"""
        br=self.br
        br.open('http://172.16.3.158/ecshop')
        # try:
        br.click_text('请登录')
        br.input_text('name=>username','wupeile')
        br.input_text('name=>password','12312')
        br.click("name=>submit")
        self.assertEqual(br.get_element('xpath=>//*[@id="ECS_MEMBERZONE"]/font/font').is_displayed(),True,u'登录失败')
        # except:
        #     print 'login failed'
        #     br.save_windows_img(br.get_image_path())