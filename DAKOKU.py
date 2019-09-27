from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_binary#chromedriverのパス設定

driver =  webdriver.Chrome()
driver.get("ログインしたいURL")#driverオブジェクト変数にURLを指定してGETレスする
driver.implicitly_wait(15)#開くまで15秒待機する

sendBox = driver.find_element_by_name('ID入力のためのフォームの名前')#ID入力するフォームのオブジェクト変数を取得

sendBox.clear()#IDフォームを初期化
sendBox.send_keys('入力したいID')#入力したいIDをフォームに入力する

loginBtn = driver.find_element_by_class_name('loginbtn')#IDボタンを取得する
loginBtn.click()#IDボタンをクリックする

sendBox = driver.find_element_by_name('Password')#パス入力するフォームのオブジェクト変数を取得
sendBox.clear()#パスフォームを初期化
sendBox.send_keys('入力したいパス')#パス入力

loginBtn = driver.find_element_by_class_name('loginbtn')
loginBtn.click()#ログインボタン押下

loginBtn = driver.find_element_by_class_name('menuGroup__name')
loginBtn.click()#タイムレコーダボタン押下

loginBtn = driver.find_element_by_id('js-punchButton')
loginBtn.click()#打刻押下

driver.quit()