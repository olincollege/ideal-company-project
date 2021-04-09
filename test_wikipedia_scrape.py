'''
Test cases for the data scrapping and manipulation code in
'wikipedia_scrape.py'

NOTE: Not all functions could be tested because
some functions require to access Wikipedia for information.

NOTE: When running pytest, please be patient.
Running the test functions that parse the data from
the wikipedia article and manipulates the data may take a while.
'''
# Import in libraries needed for testing
import pandas as pd

## Get fortune_table from 'company_info.py'
from company_info import (
    fortune_table
)

## Get all the functions from 'wikipedia_scrape.py'
from wikipedia_scrape import (
    get_company_links,
    table_to_dataframe,
    clean_dataframe,
    get_company_types,
    dictionary_to_dataframe,
    )

def test_table_to_dataframe():
    '''
    Description: Test to make sure the function 'table_to_dataframe'
    will change the table into a dataframe by checking the type
    of the function
    '''
    assert isinstance(table_to_dataframe(fortune_table), pd.DataFrame)

def test_dictionary_to_dataframe():
    '''
    Description: Test to make sure the function 'dictionary_to_dataframe'
    will change the dictionary into a dataframe by checking the type
    of the function
    '''
    assert isinstance(dictionary_to_dataframe\
                      (get_company_types(get_company_links(fortune_table))),\
                      pd.DataFrame)

def test_clean_dataframe():
    '''
    Description: Test to make sure the function cleans the dataframe
    by removing the extraneous row that lists the units for the
    Revenue and Profits Columns, dropping columns 'Profit' and 'Ref'
    and renaming the 'Headquarters[note 1]' column to 'Country'
    '''
    assert list(clean_dataframe(table_to_dataframe(fortune_table)).columns) \
        == ['Rank', 'Name', 'Industry', 'Revenue', 'Employees', 'Country']
