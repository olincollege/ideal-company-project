'''
Library for retrieving information of a Wikipedia Table
'''
## Import BeautifulSoup, requests, and pandas to convert
## the scraped data into a CSV file.
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_fortune_table(wiki_url, table_name):
    '''
    Description: Prepare the scrape by getting the access to the wikipedia page
    and set up the BeautifulSoup to pull the data from the table

    Arguments:
    - (string) wiki_url: Wikipedia URL that contains the data we need
    - (string) table_name: Name of the tag that is associated to the table

    Returns: Contents of the table in its HTML form 
    '''
    response = requests.get(wiki_url, auth=('user', 'pass'))
    soup = BeautifulSoup(response.text, 'lxml')

    return soup.find('table', {'class':table_name})

def get_company_links(table):
    dict_company_links = {}
    #list_company_links = [] <- Remove if we're not going to handle lists

    ## Put all the rows of the table into a variable
    ## to get all the company links
    fortune_rows = table.find_all('tr')

    ## Check through all the rows and get all the companny links
    ## and store them in a dictionary and library
    for company_row in fortune_rows:
        row_elements = company_row.find_all("td") # Check for all the elements in the table with a 'td' tag
        # If elements in a row are not empty, then parse the data
        if row_elements != []:
            company = row_elements[0].text.strip()
            # If found a link within the table, store it and append it to the list and dictionary
            if row_elements[0].find("a"):
                company_link = "https://en.wikipedia.org"+row_elements[0].find("a")["href"] 
                dict_company_links[company] = company_link
                #list_company_links.append(company_link) <- Remove if we're not going to handle lists
    
    return dict_company_links

def table_to_df(table):
    data = pd.read_html(str(table))

    ## Turn the list of data into a dataframe
    return data[0]

def clean_dataframe(dataframe):
    ## Clean up the dataframe
    ## Drop Duplicate Header and Reference Column
    dataframe.columns = dataframe.columns.droplevel(-1) # Drop Duplicate Header
    dataframe = dataframe.drop(columns=['Profit','Ref']) # Remove Profit & Reference Columns
    dataframe=dataframe.rename(columns = {'Country[note 1]':'Country'}) # Remove the '[note 1] from 'Country[note 1]'

    return dataframe

def get_company_types(dict_company_links):
    for company_name, company_link in dict_company_links.items():
        #print(company_name, '->', company_link)

        company_dataframe = table_to_df(get_fortune_table(company_link, 'infobox vcard'))

        company_dataframe.columns = ['header', 'value']

        company_dict = dict(zip(company_dataframe.header, company_dataframe.value))
        company_type = company_dict.get('Type')
        dict_company_links[company_name] = company_type
        
    return dict_company_links

def dictionary_to_df(dictionary):
    return pd.DataFrame(list(dictionary.items()),columns = ['Company Name','Company Type'])

def df_to_csv(dataframe, category):
    dataframe.to_csv(r'/home/softdes/Documents/softdes/ideal-company-project/' + category + '.csv', index=False)