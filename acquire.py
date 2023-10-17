# imports
import numpy as np
import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import re
import random
import time

#####################################################################################################################

def get_blog_articles():
    """
    Scrapes and structures blog data from the Codeup website.

    This function sends requests to the Codeup blog website, retrieves blog links,
    and extracts article titles and content. It then organizes the data into a
    Pandas DataFrame.

    Returns:
    pandas.DataFrame: A DataFrame containing the blog data with columns 'title' and 'article'.
    """
    # Define user agents for request headers
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
    ]

    # Randomly select a user agent
    headers = {'User-Agent': random.choice(user_agents)}

    # Base codeup blog URL
    base_url = 'https://codeup.edu/blog/'

    # Get the blog links from the base URL
    response = requests.get(base_url, headers=headers)
    base_soup = BeautifulSoup(response.text, 'html.parser')
    blog_links = [element['href'] for element in base_soup.find_all('a', class_='more-link')]

    all_blogs = []

    for link in blog_links:
        # Get a response from the blog link
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title and body
        title = soup.find('h1', class_='entry-title').text
        body = soup.find('div', class_='entry-content').text.strip()

        # Create a dictionary for each blog post
        row = {'title': title, 'article': body}
        all_blogs.append(row)

    # Cast the list of dictionaries into a pandas DataFrame
    articles = pd.DataFrame(all_blogs)

    return articles

  
  #####################################################################################################################
  
def get_news_articles():
    """
    Scrape articles from predefined categories on a website and structure the data into a Pandas DataFrame.

    Returns:
        pandas.DataFrame: A DataFrame containing the scraped articles with columns 'title', 'body', and 'category'.
    """
    # Define user agents for request headers
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"
    ]

    # Randomly select a user agent
    headers = {'User-Agent': random.choice(user_agents)}

    # Define the base URL and categories to scrape
    base_url = 'https://inshorts.com/en/read/'
    categories = ['business', 'entertainment', 'technology', 'sports']

    all_articles = pd.DataFrame(columns=['title', 'body', 'category'])
    t_sum = 0

    for category in categories:
        t_0 = time.time()
        print(f'Grabbing contents for {category}.')
        
        # Construct a URL based on the base concatenated with the category
        category_url = base_url + category
        
        # Get the response text from the constructed URL
        raw_content = requests.get(category_url, headers=headers).text
        
        # Turn the content into soup
        soup = BeautifulSoup(raw_content, 'html.parser')
        
        # Title content
        titles = [element.text for element in soup.find_all('span', itemprop='headline')]
        
        # Body content
        bodies = [element.text for element in soup.find_all('div', itemprop='articleBody')]
        
        # Create a DataFrame for the current category
        category_df = pd.DataFrame({
            'title': titles,
            'body': bodies,
            'category': category
        })
        
        # Concatenate the current category DataFrame with the overall DataFrame
        all_articles = pd.concat([all_articles, category_df], axis=0, ignore_index=True)
        
        t_n = time.time()
        t_delta = t_n - t_0
        print(f'Time to grab contents of {category}: {round(t_delta, 2)} seconds')
        t_sum += t_delta

    print('Job finished!')
    print(f'It took {round((t_sum / 60), 2)} minutes to execute scraping')

    return all_articles