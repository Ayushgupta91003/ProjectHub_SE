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


class TestAmaz2():
  def setup_method(self, method):
    self.driver = webdriver.Edge(service=Service(r"D:\4th Sem Academics\software engineering\selenium\practise\msedgedriver.exe"))
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_deewakar(self):
    self.driver.get("http://127.0.0.1:5500/jaideep/index.html")
    self.driver.set_window_size(1296, 688)
    self.driver.find_element(By.LINK_TEXT, "Recommended Products").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
    self.driver.find_element(By.LINK_TEXT, "Cart").click()
    self.driver.find_element(By.CSS_SELECTOR, ".product-item:nth-child(2) > .delete-button > button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".product-item:nth-child(2) > .buy-now-button > button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".product-item:nth-child(3) > .delete-button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".product-item:nth-child(3) > .buy-now-button > button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".go-back-button > button").click()
    self.driver.close()
  
