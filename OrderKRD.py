import checkout as checkout
import self as self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, unittest


class OrderCashKrd(unittest.TestCase):

    def test_cash_order_Krd(self) -> None:
     """Заказ за Наличку Краснодар"""
driver = webdriver.Chrome(
    executable_path='./chromedriver.exe'
)
driver.maximize_window()
driver.get("http://tokyopremium.ru/")

driver.find_element_by_xpath("/html/body/div/div/div/div[7]/div[1]/div/nav/ul/li[2]/span").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/footer/div/div[1]/div/div/div/div[2]/button").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/header/div[3]/div/div/div/a/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/section/div/div/a/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/div[2]/div/div/div/div/div[2]/div[3]/div/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/header/div[3]/div/div/div[3]/a/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/section/div/div/a/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/div[2]/div/div/div/div/div[2]/div[3]/div/div/button").click()
time.sleep(2)
driver.find_element_by_id("cartDesktopImg").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div/div/div[5]/div[1]/div/span/div/div[4]/div/div[2]/button").click()
time.sleep(2)
driver.find_element_by_id("name").click()
driver.find_element_by_id("name").send_keys("RodionQA")
driver.find_element_by_id("tt").click()
driver.find_element_by_id("tt").send_keys("+7(999)999-9999")
driver.find_element_by_id("street").click()
driver.find_element_by_id("street").send_keys(u"Думенко")
driver.find_element_by_id("house").click()
driver.find_element_by_id("house").clear()
driver.find_element_by_id("house").send_keys("12")
driver.find_element_by_id("flat").click()
driver.find_element_by_id("flat").clear()
driver.find_element_by_id("flat").send_keys("1")
driver.find_element_by_id("comment").click()
driver.find_element_by_id("comment").clear()
driver.find_element_by_id("comment").send_keys(u"ТЕСТ НЕ ГОТОВИТЬ")
driver.find_element_by_xpath("//main[@id='checkout']/div[2]/form/div/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//main[@id='checkout']/div[2]/form/div/div/div/div[5]/div/div/div/label").click()
time.sleep(2)
driver.find_element_by_id("change-of-money").click()
time.sleep(2)
driver.find_element_by_id("change-of-money").clear()
driver.find_element_by_id("change-of-money").send_keys("5000")
#driver.find_element_by_xpath("/html/body/div/div/div/div[1]/main/div[2]/form/div[2]/div/div[1]/button").click()
time.sleep(10)

#self.assertTrue("Вернуться назад" in driver.page_source)
driver.close()

class OrderCardKrd(unittest.TestCase):
    def test_card_order_Krd(self) -> None:
     """Заказ Картой Краснодар"""

driver = webdriver.Chrome(
    executable_path='./chromedriver.exe'
)
driver.maximize_window()
driver.get("http://tokyopremium.ru/")

driver.find_element_by_xpath("/html/body/div/div/div/div[7]/div[1]/div/nav/ul/li[2]/span").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/footer/div/div[1]/div/div/div/div[2]/button").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/header/div[3]/div/div/div/a/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/section/div/div/a/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/div[2]/div/div/div/div/div[2]/div[3]/div/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/header/div[3]/div/div/div[3]/a/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/section/div/div/a/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/div[2]/div/div/div/div/div[2]/div[3]/div/div/button").click()
time.sleep(2)
driver.find_element_by_id("cartDesktopImg").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div/div/div[5]/div[1]/div/span/div/div[4]/div/div[2]/button").click()
time.sleep(2)
driver.find_element_by_id("name").click()
driver.find_element_by_id("name").send_keys("RodionQA")
driver.find_element_by_id("tt").click()
driver.find_element_by_id("tt").send_keys("+7(999)999-9999")
driver.find_element_by_id("street").click()
driver.find_element_by_id("street").send_keys(u"Думенко")
driver.find_element_by_id("house").click()
driver.find_element_by_id("house").clear()
driver.find_element_by_id("house").send_keys("12")
driver.find_element_by_id("flat").click()
driver.find_element_by_id("flat").clear()
driver.find_element_by_id("flat").send_keys("1")
driver.find_element_by_id("comment").click()
driver.find_element_by_id("comment").clear()
driver.find_element_by_id("comment").send_keys(u"ТЕСТ НЕ ГОТОВИТЬ")
driver.find_element_by_xpath("//main[@id='checkout']/div[2]/form/div/div/div/div[5]/div/div/div[2]/label").click()
time.sleep(2)
#driver.find_element_by_xpath("/html/body/div/div/div/div[1]/main/div[2]/form/div[2]/div/div[1]/button").click()
time.sleep(10)
#self.assertTrue("Вернуться назад" in driver.page_source)
driver.close()


class OrderCashRost(unittest.TestCase):

    def test_cash_order_Rost(self) -> None:
     """Заказ за Наличку Ростов"""
driver = webdriver.Chrome(
    executable_path='./chromedriver.exe'
)
driver.maximize_window()
driver.get("http://tokyopremium.ru/")

driver.find_element_by_xpath("/html/body/div/div/div/div[7]/div[1]/div/nav/ul/li[1]/span").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/footer/div/div[1]/div/div/div/div[2]/button").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/header/div[3]/div/div/div/a/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/section/div/div/a/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/div[2]/div/div/div/div/div[2]/div[3]/div/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/header/div[3]/div/div/div[3]/a/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/section/div/div/a/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/div[2]/div/div/div/div/div[2]/div[3]/div/div/button").click()
time.sleep(2)
driver.find_element_by_id("cartDesktopImg").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div/div/div[5]/div[1]/div/span/div/div[4]/div/div[2]/button").click()
time.sleep(2)
driver.find_element_by_id("name").click()
driver.find_element_by_id("name").send_keys("RodionQA")
driver.find_element_by_id("tt").click()
driver.find_element_by_id("tt").send_keys("+7(999)999-9999")
driver.find_element_by_id("street").click()
driver.find_element_by_id("street").send_keys(u"Думенко")
driver.find_element_by_id("house").click()
driver.find_element_by_id("house").clear()
driver.find_element_by_id("house").send_keys("12")
driver.find_element_by_id("flat").click()
driver.find_element_by_id("flat").clear()
driver.find_element_by_id("flat").send_keys("1")
driver.find_element_by_id("comment").click()
driver.find_element_by_id("comment").clear()
driver.find_element_by_id("comment").send_keys(u"ТЕСТ НЕ ГОТОВИТЬ")
driver.find_element_by_xpath("//main[@id='checkout']/div[2]/form/div/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//main[@id='checkout']/div[2]/form/div/div/div/div[5]/div/div/div/label").click()
time.sleep(2)
driver.find_element_by_id("change-of-money").click()
time.sleep(2)
driver.find_element_by_id("change-of-money").clear()
driver.find_element_by_id("change-of-money").send_keys("5000")
#driver.find_element_by_xpath("/html/body/div/div/div/div[1]/main/div[2]/form/div[2]/div/div[1]/button").click()
time.sleep(10)

#self.assertTrue("Вернуться назад" in driver.page_source)
driver.close()

class OrderCardRost(unittest.TestCase):
    def test_card_order_Rost(self) -> None:
     """Заказ Картой Ростов"""

driver = webdriver.Chrome(
    executable_path='./chromedriver.exe'
)
driver.maximize_window()
driver.get("http://tokyopremium.ru/")

driver.find_element_by_xpath("/html/body/div/div/div/div[7]/div[1]/div/nav/ul/li[1]/span").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div/div/div[1]/footer/div/div[1]/div/div/div/div[2]/button").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/header/div[3]/div/div/div/a/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/section/div/div/a/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/div[2]/div/div/div/div/div[2]/div[3]/div/div/button").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/header/div[3]/div/div/div[3]/a/div[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/section/div/div/a/div/div").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='app']/div/main/div[2]/div/div/div/div/div[2]/div[3]/div/div/button").click()
driver.find_element_by_id("cartDesktopImg").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div/div/div[5]/div[1]/div/span/div/div[4]/div/div[2]/button").click()
driver.find_element_by_id("name").click()
driver.find_element_by_id("name").send_keys("RodionQA")
driver.find_element_by_id("tt").click()
driver.find_element_by_id("tt").send_keys("+7(999)999-9999")
driver.find_element_by_id("street").click()
driver.find_element_by_id("street").send_keys(u"Думенко")
driver.find_element_by_id("house").click()
driver.find_element_by_id("house").clear()
driver.find_element_by_id("house").send_keys("12")
driver.find_element_by_id("flat").click()
driver.find_element_by_id("flat").clear()
driver.find_element_by_id("flat").send_keys("1")
driver.find_element_by_id("comment").click()
driver.find_element_by_id("comment").clear()
driver.find_element_by_id("comment").send_keys(u"ТЕСТ НЕ ГОТОВИТЬ")
driver.find_element_by_xpath("//main[@id='checkout']/div[2]/form/div/div/div/div[5]/div/div/div[2]/label").click()
time.sleep(2)
#driver.find_element_by_xpath("/html/body/div/div/div/div[1]/main/div[2]/form/div[2]/div/div[1]/button").click()
time.sleep(10)
#self.assertTrue("Вернуться назад" in driver.page_source)
driver.close()
