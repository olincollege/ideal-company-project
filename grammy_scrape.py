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
soup = BeautifulSoup(response.text, 'lxml')

## Pull the data and save all the data into a list
grammy_table = soup.find('table', {'class':table_name})
grammy_data = pd.read_html(str(grammy_table))

## Turn the list of data into a dataframe
grammy_dataframe = grammy_data[0]

## Drop Nominees and Reference Columns
grammy_dataframe = grammy_dataframe.drop(columns=['Nominees','Ref.'])

print(grammy_dataframe)

## Transfer the grammy dataframe into a CSV file
## NOTE: When testing, please remove grammy_winner.csv file and run it again when the file is wanted
## grammy_dataframe.to_csv(r'/home/softdes/Documents/softdes/grammy-project-winner/' + 'grammy_winner.csv', index=False)