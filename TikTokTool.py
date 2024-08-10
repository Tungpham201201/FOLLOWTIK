import os
try:
    import requests,colorama,prettytable
except:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("pip install prettytable")
import threading, requests, ctypes, random, json, time, base64, sys, re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
os.system("cls" if os.name == "nt" else "clear")

print(f'''\033[1;32m
    ████████╗██╗██╗░░██╗████████╗░█████╗░██╗░░██╗
    \033[1;33m╚══██╔══╝██║██║░██╔╝╚══██╔══╝██╔══██╗██║░██╔╝
    ░░░██║░░░██║█████═╝░░░░██║░░░██║░░██║█████═╝░
   \033[1;36m ░░░██║░░░██║██╔═██╗░░░░██║░░░██║░░██║██╔═██╗░
    ░░░██║░░░██║██║░╚██╗░░░██║░░░╚█████╔╝██║░╚██╗
   \033[1;97m ░░░╚═╝░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
    ░░░╚═╝░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

      \033[1;34mTool Buff tiktok Vip by: Roasted_anonymous
        [-----------------------------------]
        \033[1;33m2.YouTube: 🔱 ROASTED_ANONYMOUS 🔱
        \033[1;36m3.Zalo: 0983544223
        \033[1;36m4.Facebook: Phạm Thanh Tùng
        \033[0;35m5.Telegram: Roasted2001
      [====================================]
        \033[31m ╰☜ Cảm ơn đã sử dụng tool của tôi ☞╯ \n\033[31m             ╰☜ Chúc một ngày tốt lành ☞╯''')

class Zefoy:
    def __init__(self):
        self.base_url = 'https://zefoy.com/'
        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
        self.session = requests.Session()
        self.captcha_1 = None
        self.captcha_ = {}
        self.service = 'Comments Hearts'
        self.video_key = None
        self.services = {}
        self.services_ids = {}
        self.services_status = {}
        self.url = 'None'
        self.text = 'Tool Zefoy'
        url1=input("\033[1;33m       => link video:  ")
      
        self.url=url1
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.set_window_size(1024, 650)

Views = 0
Hearts = 0
Followers = 0

def countdown(t):
	while t: 
		mins, secs = divmod(t, 60) 
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print(timer, end="\r") 
		sleep(1) 
		t -= 1

def beautify(arg):
    return format(arg, ',d').replace(',', '.')

def title1():
    global Views
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        os.system(f'title TikTok Viewer by ShawnSavour ^| Views Sent: {beautify(Views)} ^| Elapsed Time: {time_elapsed}')

def title2():
    global Hearts
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        os.system(f'title TikTok Viewer by ShawnSavour ^| Hearts Sent: {beautify(Hearts)} ^| Elapsed Time: {time_elapsed}')

def title3():
    global Followers
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        os.system(f'title TikTok Viewer by ShawnSavour ^| Followers Sent: {beautify(Followers)} ^| Elapsed Time: {time_elapsed}')
    

def loop1():
    global Views
    countdown(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
        countdown(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vidUrl)
        countdown(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click()
        countdown(3)
        Viewnum = driver.find_element_by_xpath('//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div/div/form/button').text.split()
        countdown(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div/div/form/button").click()
        countdown(5)
        driver.refresh()
        Views += 1800
        print(datetime.now().strftime("%H:%M:%S"), "Successful", Viewnum[0], "+", Views)
        countdown(270)
        loop1()
    except:
        print("> An error occured. Trying again...", datetime.now().strftime("%H:%M:%S"))
        driver.refresh()
        loop1()

def loop2():
    global Hearts
    countdown(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
    except:
        print("> Solve the captcha!")
        driver.refresh()
        loop2()
    try:
        countdown(2)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/div/div/form/div/input').send_keys(vidUrl)
        countdown(1)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/div/div/form/div/div/button').click()
        countdown(5)
        driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
        countdown(6)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text.split()
        Hearts += int(hearts[0])
        countdown(5)
        driver.refresh()
        countdown(640)
        loop2()
    except:
        print("> An error occured. Trying again...")
        driver.refresh()
        loop2()

def loop3():
    global Followers
    countdown(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click()
        countdown(2)
        driver.find_element_by_xpath('//*[@id="sid"]/div/div/div/form/div/input').send_keys(vidUrl)
        countdown(1)
        driver.find_element_by_xpath('//*[@id="sid"]/div/div/div/form/div/div/button').click()
        countdown(5)
        folls = driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').text.split()
        Followers += int(folls[0])
        print(folls)
        countdown(2)
        driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()        
        countdown(6)
        driver.refresh()
        countdown(310)
        loop3()
    except:
        print("> An error occured. Now will retry again")
        driver.refresh()
        loop3()

system("cls")
print(pyfiglet.figlet_format("Successful", font="slant"))

if auto == 1:
    driver.get("https://zefoy.com/")
    a = threading.Thread(target=title1)
    b = threading.Thread(target=loop1)
    a.start()
    b.start()
elif auto == 2:
    driver.get("https://zefoy.com/")
    a = threading.Thread(target=title2)
    b = threading.Thread(target=loop2)
    a.start()
    b.start()
elif auto == 3:
    driver.get("https://zefoy.com/")
    a = threading.Thread(target=title3)
    b = threading.Thread(target=loop3)
    a.start()
    b.start()
else:
    print("Input between 1-3")




