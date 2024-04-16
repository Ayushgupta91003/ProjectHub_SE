# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.edge.service import Service

class TestAmazon1():
  def setup_method(self, method):
      self.driver = webdriver.Edge(service=Service(r"D:\4th Sem Academics\software engineering\selenium\practise\msedgedriver.exe"
))

  def teardown_method(self, method):
    self.driver.quit()

  def test_jaideep(self):
    self.driver.get("http://127.0.0.1:5500/jaideep/index.html")
    self.driver.set_window_size(1296, 688)
    self.driver.find_element(By.NAME, "search").click()
    self.driver.find_element(By.NAME, "search").send_keys("Laptop")
    self.driver.find_element(By.CSS_SELECTOR, ".ml-2").click()
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.ID, "navbarDropdown").click()
    self.driver.find_element(By.LINK_TEXT, "Recommended Products").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
    self.driver.find_element(By.LINK_TEXT, "Profile").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-go-back").click()
    self.driver.find_element(By.LINK_TEXT, "Cart").click()
    self.driver.find_element(By.CSS_SELECTOR, ".go-back-button > button").click()
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
    self.driver.find_element(By.CSS_SELECTOR, "a > img").click()
    self.driver.find_element(By.LINK_TEXT, "Buy Now").click()
    self.driver.find_element(By.CSS_SELECTOR, ".payment-method:nth-child(1) > p").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".payment-method:nth-child(2) > p").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".payment-method:nth-child(3) > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".payment-method:nth-child(4) > p").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
    self.driver.close()

