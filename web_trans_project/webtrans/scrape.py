import requests
from bs4 import BeautifulSoup
import json
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from . import translator

def webtrans(url,lang,tag,div):
    # Set up Firefox options
    options = Options()
    options.headless = True

    # Create a new instance of the Firefox driver with headless option
    driver = webdriver.Firefox(options=options)
    # url='https://www.taxgoglobal.com/pricing'
    driver.get(url)
    filename = url.rsplit('/', 1)[-1]
    if filename == "":
        filename='home'
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.text)
    # print('...........')
    h= ['h1','h2','h3','h4','h5','h6']
    if 'h' in tag:
        tag.remove('h')
        tag.extend(h)
    links = [link.text for link in soup.find_all(tag)]
    #add div-classes
    for classes in div:
        links1 = [link.text for link in soup.find_all(['div'],class_=re.compile(classes,re.IGNORECASE))]
        links.extend(links1)
    
    links2 = [link.text for link in soup.find_all('button')]
    links.extend(links2)

    my_dict={}
    f=open(f'{filename}.txt','w',encoding='utf-8')


    for element in links:
        my_dict[element.strip()] = True

    # Convert the keys of the dictionary back to a list
    new_list = list(my_dict.keys())
    d=new_list.copy()

    for i in d:
        f.write(i+'\n')

    f.close()
    print(lang)
    return translator.trans(f'{filename}.txt',lang)