## Import BeautifulSoup, requests, and pandas to convert
## the scraped data into a CSV file.
from bs4 import BeautifulSoup
import requests
import pandas as pd

## Get the wikipedia link
## and find the identification of the table
wiki_url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year"
table_name = "wikitable sortable"

## Prepare the scrape by getting the access to the wikipedia page
## and set up the BeautifulSoup to pull the data
response = requests.get(wiki_url, auth=('user', 'pass'))
soup = BeautifulSoup(response.text, 'html.parser')

## Pull the data and save all the data into a list
grammy_table = soup.find('table', {'class':table_name})
grammy_data = pd.read_html(str(grammy_table))

## Turn the list of data into a dataframe
grammy_dataframe = grammy_data[0]

## For testing purposes
## print(grammy_dataframe["Winner(s)"][3])