## From the dataframe, get the nationalities
## and return a list

## Import itertools for iteration
## Import grammy_scrape file for the dataframe
import itertools
from grammy_scrape import grammy_dataframe

def main():
    '''
    Gets the nationalities from the dataframe column
    and puts them into a list for plotting

    Arguments: None

    Returns: type <list>: all the nationalities by name
    '''
    nationalities_list = grammy_dataframe["Nationality"].tolist()
    nationalities_list = [nationality.split('\xa0') for nationality in nationalities_list]
    
    return list(itertools.chain.from_iterable(nationalities_list))

## For testing
## print(main())