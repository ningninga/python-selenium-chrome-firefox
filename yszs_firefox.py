#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020/12/2 15:01
# Project: 
# @Author: ningninga
# @Email : 

import time

from selenium import webdriver

driver = webdriver.Firefox()  

driver.get("http://101.200.166.86:8000/ysb_toolkit/toolkit_index")
time.sleep(2)
driver.find_element_by_id("username").send_keys("xiluo")
driver.find_element_by_id("password").send_keys("ys123456")
driver.find_element_by_css_selector("#login-common-body > div.login-footer > button").click()


driver.find_element_by_css_selector("body > div.index-body > div:nth-child(2) > div.li-body > div > ul > li:nth-child(1) > a").click()
# 关闭标签
driver.find_element_by_css_selector("body > div.zb-num-left > div:nth-child(12) > a").click()
driver.find_element_by_css_selector("body > div.zb-new-left > div:nth-child(4) > a").click()

driver.find_element_by_css_selector("#frxb > option:nth-child(2)").click()

driver.find_element_by_css_selector("#pro > option:nth-child(8)").click()
driver.find_element_by_css_selector("#city > option:nth-child(2)").click()
driver.find_element_by_css_selector("#con > option:nth-child(6)").click()

driver.find_element_by_css_selector("#jbsx-model > div:nth-child(7) > div.bqk-line-body > div > div:nth-child(1)").click()


driver.find_element_by_css_selector("#fxzb").click()


driver.find_element_by_css_selector("#fxzb-model > div:nth-child(1) > div.bqk-line-body > div > div:nth-child(2) > input:nth-child(1)").send_keys(1)

# 确认筛选
driver.find_element_by_css_selector("#dw-model > div:nth-child(1) > div.button.select-fill").click()


# 查询结果
driver.find_element_by_css_selector("#dw-model > div:nth-child(2) > div").click()
time.sleep(10)
driver.quit()  # 关闭driver

