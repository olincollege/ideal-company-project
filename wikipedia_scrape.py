## Import BeautifulSoup, requests, and pandas to convert
## the scraped data into a CSV file.
from bs4 import BeautifulSoup
import requests
import pandas as pd

## Get the wikipedia link
## and find the identification of the table
wiki_url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
table_name = "wikitable sortable"

## Prepare the scrape by getting the access to the wikipedia page
## and set up the BeautifulSoup to pull the data
response = requests.get(wiki_url, auth=('user', 'pass'))
soup = BeautifulSoup(response.text, 'lxml')

## Pull the data and save all the data into a list
fortune_table = soup.find('table', {'class':table_name})
fortune_data = pd.read_html(str(fortune_table))

## Turn the list of data into a dataframe
fortune_dataframe = fortune_data[0]

## Clean up the dataframe
## Drop Duplicate Header and Reference Column
fortune_dataframe.columns = fortune_dataframe.columns.droplevel(-1) # Drop Duplicate Header
fortune_dataframe = fortune_dataframe.drop(columns=['Profit','Ref']) # Remove Profit & Reference Columns
fortune_dataframe=fortune_dataframe.rename(columns = {'Country[note 1]':'Country'}) # Remove the '[note 1] from 'Country[note 1]'

## Transfer the top 50 of the fortune 500 companies dataframe into a CSV file
## NOTE: When testing, please remove company_winner.csv file and run it again when the file is wanted
## company_dataframe.to_csv(r'/home/softdes/Documents/softdes/company-project-winner/' + 'company_winner.csv', index=False)