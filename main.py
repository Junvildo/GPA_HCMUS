from selenium import webdriver


f=open("./login_info.txt","r")
lines=f.readlines()
username=lines[0]
password=lines[1]
f.close()


browser = webdriver.Firefox()
browser.get('https://learning.hvthao.com/portal')

browser.find_element("id","eid").send_keys(username)
browser.find_element("id","pw").send_keys(password)
browser.find_element("id","submit").click()

