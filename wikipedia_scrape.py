'''
Library for retrieving information of a Wikipedia Table
'''
## Import BeautifulSoup, requests, and pandas to convert
## the scraped data into a CSV file.
from bs4 import BeautifulSoup
import requests
import pandas

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

def table_to_dataframe(table):
    '''
    Description: Converts the HTML table of all the contents of the
    top 50 of the Fortune 500 into a dataframe

    Arguments:
    - (HTML) table: a table of all the scraped contents from the
    Wikipedia article containing the information about the top
    50 companies of the Global Fortune 500.

    Returns: a formatted dataframe
    containing all the of the top 50 companies of the Global Fortune 500.
    '''
    ## Convert the table into a string
    data = pandas.read_html(str(table))

    ## Turn the data string into a dataframe
    return data[0]

def clean_dataframe(dataframe):
    '''
    Description: Clean up the dataframe table by
    dropping the unnecessary second header that contains
    the measurement units for the Profit and Revenue,
    dropping the Profits section and Reference Sections,
    and removing the '[note 1]' in the name of the Country column

    Arguments:
    - (dataframe) dataframe: a formatted dataframe containing
    the information about the top 50 companies of the Global Fortune 500.

    Returns: a formatted dataframe
    containing all the of the top 50 companies of the Global Fortune 500
    without any of the aformentioned rows and columns
    '''
    # Drop Duplicate Header
    dataframe.columns = dataframe.columns.droplevel(-1)
    # Remove Profit & Reference Columns
    dataframe = dataframe.drop(columns=['Profit','Ref'])
    # Remove the '[note 1]' from 'Country[note 1]'
    dataframe = dataframe.rename(columns = {'Country[note 1]':'Country'})

    return dataframe

def get_company_links(table):
    '''
    Description: Go through the parsed table,
    find all the links of the companies,
    and store them in a dictionary alongisde with
    the company of the name they are associated with.

    Arguments
    - (HTML) table: a table of all the scraped contents from the
    Wikipedia article containing the information about the top
    50 companies of the Global Fortune 500.

    Returns: a dictionary of all the company links with the
    company names as the key and the links as their stored values.
    '''
    # Empty dictionary to store all the company links
    dictionary_company_links = {}

    ## Put all the rows of the table into a variable
    ## to get all the company links
    fortune_rows = table.find_all('tr')

    ## Check through all the rows and get all the companny links
    ## and store them in a dictionary and library
    for company_row in fortune_rows:
        # Check for all the elements in the table with a 'td' tag
        row_elements = company_row.find_all("td")
        # If elements in a row are not empty, then parse the data
        if row_elements != []:
            company = row_elements[0].text.strip()
            # If found a link within the table, store it and append it to the dictionary
            if row_elements[0].find("a"):
                company_link = "https://en.wikipedia.org"+row_elements[0].find("a")["href"]
                dictionary_company_links[company] = company_link

    return dictionary_company_links

def get_company_types(dict_company_links):
    '''
    Description: from the parsed dictionary with all the companies
    and their links, get the company types from all the companies
    and store the types of companies alongside with the company name

    Arguments:
    - (dictionary) dict_company_links: a dictionary of all the
    company links with the company names as the key and the links as their stored values.

    Returns: a dictionary of all the company links with the
    company names as the keys and the types as their stored values.
    '''
    # Empty dictionary to contain all the company types
    dictionary_company_types = {}

    # Go through all the companies in the dictionary
    for company_name, company_link in dict_company_links.items():
        # Get the dataframe table of the information box with the type of company
        company_dataframe = table_to_dataframe(get_fortune_table(company_link, 'infobox vcard'))
        # Replace the column names '1' and '2' to 'header' and 'value'
        company_dataframe.columns = ['header', 'value']
        # Change the dataframe into a dictionary
        company_dictionary = dict(zip(company_dataframe.header, company_dataframe.value))
        # In the dictionary, find the value associated with the 'Type' key
        company_type = company_dictionary.get('Type')
        # Store the key 'Type' value into a dictionary
        dictionary_company_types[company_name] = company_type
    return dictionary_company_types

def dictionary_to_dataframe(dictionary):
    '''
    Description: Turns the company types dictionary into a dataframe
    and assigns the column names as 'Company Name' and 'Company Type'

    Arguments: a dictionary a dictionary of all the company links with the
    company names as the keys and the types as their stored values.

    Returns: a dataframe with the columns "Company Name" and "Company Type"
    '''
    return pandas.DataFrame(list(dictionary.items()),columns = ['Company Name','Company Type'])

def dataframe_to_csv(dataframe, category):
    '''
    Description: Turn the dataframe into a CSV file for analysis on the final paper

    Arguments:
    - dataframe: a dataframe of either the total companies information or
    each respective company types
    - category: the file name and type that the dataframe is converting to

    Returns: A CSV file containing either the total companies information or
    each respective company types
    '''
    ## CHANGE THE TEXT IN HERE AND CHANGE YOUR FILE DIRECTORY 
    dataframe.to_csv(r'/home/softdes/Documents/softdes/ideal-company-project/' \
        + category + '.csv', index=False)
