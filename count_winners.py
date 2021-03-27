## From the dataframe, get the winners
## and return a list
## TODO: update whatever this function
## is supposed to accomplish and the 
## unknowns in line 22

## Import itertools for iteration
## Import grammy_scrape file for the dataframe
import itertools
from grammy_scrape import grammy_dataframe

def list_of_winners():
    '''
    Get the winners from the grammy_dataframe
    and put it into a list for comparison
    to the list of Performing Artists

    Arguments: None

    Returns: type <list>: all the winners by name

    TODO: not completely sure how to seperate the names
    since some names are bunched together with MANY
    possible names that can't be seperated
    '''
    winners_list = grammy_dataframe["Winner(s)"].tolist()

    return winners_list

## For testing
## print(list_of_winners())