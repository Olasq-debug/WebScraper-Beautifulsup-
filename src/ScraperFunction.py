from bs4 import BeautifulSoup
import requests
from .webUrls import *
import pandas as pd
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()

joblist = []

# A function that scrape arc.dev website
def ArcScraper():
    res = requests.get(arcUrl)
    soup = BeautifulSoup(res.text, 'html.parser')
    jobs = soup.find_all('div', {'class':'sc-a6ebedfc-0 gPvyTm job-card'})
    for job in jobs:
        jobposts = {
        'title' : job.find('a', {'class': 'job-title'}).text,
        'link' : 'https://arc.dev/remote-jobs' + job.find('a', {'class': 'job-title'})['href'],
        'skills' : job.find('a', {'class': 'sc-a6ebedfc-1 ddFunq category'})['href']
        }
        joblist.append(jobposts)
    return 

 #A function that scrape VanHack website
def VanHackScraper():
    driver.get(vanHackUrl)
    time.sleep(4)
    res = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(res, 'html.parser')
    jobs = soup.find_all('div', {'class': 'sc-coQLGf gRuMdb job-card'})
    for job in jobs:
        jobposts = {
        'title' : job.find('div', {'class': 'sc-gKXmdW clEcrP'}).text,
        'link' : 'https://vanhack.com/' + job.find('a', {'class': 'sc-iRGnHV huGkU'})['href'],
        'description' : job.find('div', {'class': 'sc-iBlNuT fodIfN'}).text,
        }
        joblist.append(jobposts)
    return

# A function that scrape Turing website
def TuringScraper():
    driver.get(TuringUrl)
    res = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(res, 'html.parser')
    jobs = soup.find_all('div', {'class': 'Carousel_container__bLTOD'})
    for job in jobs:
        jobposts = {
        'title' : job.find('h5', {'class': 'JobOpeningCard_title___0bSL'}).text,
        'link' : 'https://www.turing.com/jobs' + job.find('a', {'class': 'JobOpeningCard_root__5Ckjy'})['href'], 
        #'description' : job.find('div', {'class':'JobOpeningCard_description__zIqRj'}).span.text
        }
        joblist.append(jobposts)
    return

# A function that scrape jremote website
def jRemoteScraper():
    res = requests.get(jremoteUrl)
    soup = BeautifulSoup(res.text, 'html.parser')
    jobs = soup.find_all('div', {'class': 'new-job-item__JobItemWrapper-sc-1qa4r36-0 hxecsD'})
    for job in jobs:
        jobposts = {
        'title' : job.find('h3', class_='new-job-item__JobTitle-sc-1qa4r36-8 iNuReR').text,
        'link' : 'https://justremote.co/' + job.find('a', class_='new-job-item__JobMeta-sc-1qa4r36-7 eFiLvL')['href'],
        }
        joblist.append(jobposts)
    return

# A function that scrape remotive website
def RemotiveScraper():
    res = requests.get(remotiveUrl)
    soup = BeautifulSoup(res.text, 'html.parser')
    jobs = soup.find_all('li', {'class': 'tw-cursor-pointer'})
    for job in jobs:
        jobposts = {
        'title' : job.find('span', {'class': 'remotive-bold'}).text,
        'link' : 'https://remotive.com/' + job.find('a', {'class': 'remotive-url-visit tw-block md:tw-flex'})['href'],
        'skills' : job.find('a', {'class': 'job-tile-category remotive-url'}).text
        }
        joblist.append(jobposts)
    return
    

ArcScraper()
jRemoteScraper()
RemotiveScraper()
TuringScraper()
VanHackScraper()

