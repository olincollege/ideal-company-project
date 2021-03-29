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
company_table = soup.find('table', {'class':table_name})
company_data = pd.read_html(str(company_table))

## Turn the list of data into a dataframe
company_dataframe = company_data[0]

## Clean up the dataframe
## Drop Duplicate Header and Reference Column
company_dataframe.columns = company_dataframe.columns.droplevel(-1) # Drop Duplicate Header
company_dataframe = company_dataframe.drop(columns=['Profit','Ref']) # Remove Profit & Reference Columns
company_dataframe=company_dataframe.rename(columns = {'Country[note 1]':'Country'}) # Remove the '[note 1] from 'Country[note 1]'

print(company_dataframe)

## Transfer the company dataframe into a CSV file
## NOTE: When testing, please remove company_winner.csv file and run it again when the file is wanted
## company_dataframe.to_csv(r'/home/softdes/Documents/softdes/company-project-winner/' + 'company_winner.csv', index=False)