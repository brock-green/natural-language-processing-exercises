# imports
import numpy as np
import os
import requests
from bs4 import BeautifulSoup
import re
import random

def get_blog_articles():
    '''
    
    '''
    # define some user_agents to spoof the request headers
    user_agents = [
      "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
      "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
      "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
      ]


    # randomize the user agent
    random_user_agent = random.choice(user_agents)
    
    # record the urls for at least 5 distinct blog posts.
    url0 = 'https://codeup.edu/featured/apida-heritage-month/'
    url1 = 'https://codeup.edu/featured/women-in-tech-panelist-spotlight/'
    url2 = 'https://codeup.edu/featured/women-in-tech-rachel-robbins-mayhill/'
    url3 = 'https://codeup.edu/codeup-news/women-in-tech-panelist-spotlight-sarah-mellor/   '
    url4 = 'https://codeup.edu/events/women-in-tech-madeleine/'
    
    # create response object
    headers = {'User-Agent': random_user_agent}
    response0 = requests.get(url0, headers=headers)
    response1 = requests.get(url1, headers=headers)
    response2 = requests.get(url2, headers=headers)
    response3 = requests.get(url3, headers=headers)
    response4 = requests.get(url4, headers=headers)
    
    # create soup object
    soup0 = BeautifulSoup(response0.text, 'html.parser')
    soup1 = BeautifulSoup(response1.text, 'html.parser')
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    soup3 = BeautifulSoup(response3.text, 'html.parser')
    soup4 = BeautifulSoup(response4.text, 'html.parser')
    
    # use soup.select to find the title
    title0 = (soup0.h1.text)
    title1 = (soup1.h1.text)
    title2 = (soup2.h1.text)
    title3 = (soup3.h1.text)
    title4 = (soup4.h1.text)
    
    # create vars for lists of all p elements
    list_of_p0 = soup0.find_all('p')
    list_of_p1 = soup1.find_all('p')
    list_of_p2 = soup2.find_all('p')
    list_of_p3 = soup3.find_all('p')
    list_of_p4 = soup4.find_all('p')
    
    # create vars to hold the contents of the blog posts. Use list comprehension to join the list of elements into a string.
    contents_blog0 = ' '.join([element.text for element in list_of_p0])
    contents_blog1 = ' '.join([element.text for element in list_of_p1])
    contents_blog2 = ' '.join([element.text for element in list_of_p2])
    contents_blog3 = ' '.join([element.text for element in list_of_p3])
    contents_blog4 = ' '.join([element.text for element in list_of_p4])
    
    # Create a dictionary of title and content for each blog post
    blog0 = {'title': title0, 'content': contents_blog0}
    blog1 = {'title': title1, 'content': contents_blog1}
    blog2 = {'title': title2, 'content': contents_blog2}
    blog3 = {'title': title3, 'content': contents_blog3}
    blog4 = {'title': title4, 'content': contents_blog4}
    
    # create a list of dictionaries for each blog post
    blogs = [blog0, blog1, blog2, blog3, blog4]
    
    return blogs


def get_news_articles():
  '''
  
  '''
  # define some user_agents to spoof the request headers
  user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
    ]


  # randomize the user agent
  random_user_agent = random.choice(user_agents)
  
  