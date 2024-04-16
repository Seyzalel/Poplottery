from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://poplottery.com/#/login")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "userNumber")))
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.NAME, "userNumber")).click().perform()
time.sleep(2)

driver.find_element(By.NAME, "userNumber").send_keys("13997779067")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Senha'][type='password']")))
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Senha'][type='password']").send_keys("17102005seyzalel")

login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.active")))
actions.move_to_element(login_button).click().perform()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.van-button__text")))
confirm_button = driver.find_element(By.CSS_SELECTOR, "span.van-button__text")
actions.move_to_element(confirm_button).click().perform()

print("Login bem sucedido.")
driver.quit()