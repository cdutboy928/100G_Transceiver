# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.firefox.service import Service  # 修改为 Firefox 的 Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # 导入 Keys 用于模拟键盘输入
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
driver_path = os.getenv('GECKODRIVER_PATH')  # 确保在 .env 文件中设置了 GECKODRIVER_PATH
target_url = os.getenv('TARGET_URL')  # 确保在 .env 文件中设置了 TARGET_URL

# Initialize WebDriver for Firefox
service = Service(driver_path)  # 创建 Firefox 的 Service
browser = webdriver.Firefox(service=service)  # 修改为 Firefox 浏览器

try:
    # Open the target webpage
    browser.get(target_url)

    # 等待登录表单加载
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'nz-input-group.ng-tns-c177-0 > input:nth-child(2)')))  # 替换为实际的用户名输入框的选择器

    # 输入用户名和密码
    username_input = browser.find_element(By.CSS_SELECTOR, 'nz-input-group.ng-tns-c177-0 > input:nth-child(2)')  # 替换为实际的用户名输入框的选择器
    password_input = browser.find_element(By.CSS_SELECTOR, 'nz-input-group.ng-tns-c177-1 > input:nth-child(2)')  # 替换为实际的密码输入框的选择器
    username_input.send_keys=os.getenv('')  # 替换为实际的用户名
    password_input.send_keys=os.getenv(('')  # 替换为实际的密码

    # 提交表单
    password_input.send_keys(Keys.RETURN)  # 模拟按下回车键提交表单

    # 登录成功后，导航到指定的 URL
    browser.get('http://118.187.15.2:8089/#/sdn/business/business-info/Tunnel-Site-1688835019528867840%23Ne-1688854328804249600%23LINECARD-1-1%23PORT-1-1-C1-Site-1688835019101048832%23Ne-1688854328921690112%23LINECARD-1-1%23PORT-1-1-C1?tabKey=0')  # 导航到目标网址

    # 等待页面加载完成
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cdk-overlay-4 > nz-modal-container > div > div > div.ant-modal-body.ng-tns-c213-55 > div > div.ant-col.ant-col-13 > div > pm-list-panel > nz-tabset > div > div.ant-tabs-tabpane.ng-star-inserted.ant-tabs-tabpane-active > div > nz-table > nz-spin > div > div > nz-table-inner-default > div > table > tbody > tr:nth-child(4) > td:nth-child(2)')))  # 增加等待时间

    # Get the page source
    page_source = browser.page_source

    # Parse the HTML content
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract the first value using the CSS selector
    value1_element = soup.select_one('#cdk-overlay-4 > nz-modal-container > div > div > div.ant-modal-body.ng-tns-c213-55 > div > div.ant-col.ant-col-13 > div > pm-list-panel > nz-tabset > div > div.ant-tabs-tabpane.ng-star-inserted.ant-tabs-tabpane-active > div > nz-table > nz-spin > div > div > nz-table-inner-default > div > table > tbody > tr:nth-child(4) > td:nth-child(2)')
    value1 = value1_element.text.strip() if value1_element else None

    # Extract the second value using the CSS selector (to be defined)
    value2_element = soup.select_one('#your_css_selector_for_value2')  # Replace with actual selector
    value2 = value2_element.text.strip() if value2_element else None

    # Save the data to a CSV file
    with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Value1', 'Value2'])  # Include headers as necessary
        writer.writerow([value1, value2])      # Replace with actual variables

finally:
    # Close the browser
    browser.quit()
