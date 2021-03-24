from selenium import webdriver
import random
from tkinter import *
import time

root = Tk()
root.geometry('1500x290+200+100')
root.configure(background = 'Red')

root.title('What Am I Doing With My Life?')

links = []

PATH = 'C:\ChromeDriver\chromedriver_win32(89)\chromedriver.exe'
url = "https://www.youtube.com/results?search_query=hentai"
driver = webdriver.Chrome(PATH)
driver.get(url)
num = 1
#source = driver.page_source
#print(source)
#print(driver.page_source)

while True:
    a = driver.execute_script('return document.documentElement.scrollHeight')
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')
    time.sleep(1.5)
    b = driver.execute_script('return document.documentElement.scrollHeight')
    #print(driver.execute_script('return document.documentElement.scrollHeight'))
    print(a)
    print(b)
    if a == b:
        break

plum = driver.find_elements_by_tag_name("a")

tex = Text(master = root, width = 200, height = 1, font = ('Times New Roman', 22))
tex.grid(column = 4)


for link in plum:
    zoo = link.get_attribute('href')
    if zoo != None:
        if zoo.find('watch?v') != -1:
            links.append(zoo)
    else:
        pass
print(links)
def Main():
    num1 = random.randint(0, len(links)-1)
    tex.delete('1.0', END)
    tex.insert(END, links[num1])
button = Button(root, text = 'Random Link', width = 20, height= 2, command = Main)
button.grid(column = 4)
root.mainloop()
