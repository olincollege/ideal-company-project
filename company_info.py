'''
Use the functions in 'wikipedia_scrape.py' to scrape data from the
Global Fortune 500 Top 50 Companies table into csv files
'''
## Get all the functions from 'wikipedia_scrape.py'
from wikipedia_scrape import get_fortune_table, get_company_links,\
    table_to_dataframe, clean_dataframe, get_company_types,\
    dictionary_to_dataframe, dataframe_to_csv

## Scrape the data from the Global Fortune 500 Top 50 Companies data into a table
fortune_table = get_fortune_table(\
    'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue','wikitable sortable')

## Get data from the base table and into a CSV file for plotting
dataframe_to_csv(clean_dataframe(table_to_dataframe(fortune_table)),'company_total')

## Get all the company types and store the information in a CSV file for plotting
dataframe_to_csv(dictionary_to_dataframe(get_company_types(get_company_links(\
    fortune_table))), 'company_type')
    