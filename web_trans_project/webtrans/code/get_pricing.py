import requests
from bs4 import BeautifulSoup
import json
from deep_translator import GoogleTranslator
import re

from selenium import webdriver
from translator import trans

def webtrans(url):
    driver = webdriver.Firefox()
    # url='https://www.taxgoglobal.com/pricing'
    driver.get(url)
    filename = url.rsplit('/', 1)[-1]
    if filename == "":
        filename='home'
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.text)
    # print('...........')
    links = [link.text for link in soup.find_all(['h1','h2','h3','h4','a','span','p','br'])]

    links2 = [link.text for link in soup.find_all('button')]
    links.extend(links2)

    my_dict={}
    f=open(f'{filename}.txt','w')


    for element in links:
        my_dict[element.strip()] = True

    # Convert the keys of the dictionary back to a list
    new_list = list(my_dict.keys())
    d=new_list.copy()

    for i in d:
        f.write(i+'\n')

    f.close()
    trans(f'{filename}.txt')