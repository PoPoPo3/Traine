# # -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
# import unittest, time, re
#
#
# class CashOrderKrd(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(30)
#         self.base_url = "https://www.google.com/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
#
#     def test_cash_order_krd(self):
#         driver = self.driver
#         driver.maximize_window()
#         driver.get("https://tokyopremium.ru/")
#         driver.find_element_by_xpath("/html/body/div/div/div/div[7]/div[1]/div/nav/ul/li[2]/span").click()
#         driver.find_element_by_xpath(
#             "/html/body/div/div/div/div[1]/footer/div/div[1]/div/div/div/div[2]/button").click()
#         driver.find_element_by_xpath("//div[@id='app']/div/header/div[3]/div/div/div/a/div[2]").click()
#         driver.find_element_by_xpath("//div[@id='app']/div/main/section/div/div/a/div/div").click()
#         time.sleep(3)
#         driver.find_element_by_xpath(
#             "//div[@id='app']/div/main/div[2]/div/div/div/div/div[2]/div[3]/div/div/button").click()
#         driver.find_element_by_xpath("//div[@id='app']/div/header/div[3]/div/div/div[3]/a/div[2]").click()
#         driver.find_element_by_xpath("//div[@id='app']/div/main/section/div/div/a/div/div").click()
#         driver.find_element_by_xpath(
#             "//div[@id='app']/div/main/div[2]/div/div/div/div/div[2]/div[3]/div/div/button").click()
#         driver.find_element_by_id("cartDesktopImg").click()
#         driver.find_element_by_xpath(
#             "/html/body/div/div/div/div[5]/div[1]/div/span/div/div[4]/div/div[2]/button").click()
#         driver.find_element_by_id("name").click()
#         driver.find_element_by_id("name").send_keys("RodionQA")
#         driver.find_element_by_id("tt").click()
#         driver.find_element_by_id("tt").send_keys("+7(999)999-9999")
#         driver.find_element_by_id("street").click()
#         driver.find_element_by_id("street").send_keys(u"Думенко")
#         driver.find_element_by_id("house").click()
#         driver.find_element_by_id("house").clear()
#         driver.find_element_by_id("house").send_keys("12")
#         driver.find_element_by_id("flat").click()
#         driver.find_element_by_id("flat").clear()
#         driver.find_element_by_id("flat").send_keys("1")
#         driver.find_element_by_id("comment").click()
#         driver.find_element_by_id("comment").clear()
#         driver.find_element_by_id("comment").send_keys(u"ТЕСТ НЕ ГОТОВИТЬ")
#         driver.find_element_by_xpath("//main[@id='checkout']/div[2]/form/div/div/div").click()
#         driver.find_element_by_xpath("//main[@id='checkout']/div[2]/form/div/div/div/div[5]/div/div/div/label").click()
#         driver.find_element_by_id("change-of-money").click()
#         driver.find_element_by_id("change-of-money").clear()
#         driver.find_element_by_id("change-of-money").send_keys("5000")
#
#     def is_element_present(self, how, what):
#         try:
#             self.driver.find_element(by=how, value=what)
#         except NoSuchElementException as e:
#             return False
#         return True
#
#     def is_alert_present(self):
#         try:
#             self.driver.switch_to_alert()
#         except NoAlertPresentException as e:
#             return False
#         return True
#
#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to_alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally:
#             self.accept_next_alert = True
#
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)
#
#
# if __name__ == "__main__":
#     unittest.main()
