import pandas as pd 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt

# Dataset: https://www.kaggle.com/datasets/shivamb/netflix-shows
def file_reader(file_name):  
    '''
    Reads the dataset as a dataframe and uses the specified columns to be represented.
    Initial Order: ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']
    Created Order: {'show_id': ('title', 'type', 'director', 'cast', 'description')}
    
    Parameters
    ----------
    file_name: file path
    
    Returns
    -------
    tuple with:
    the reader dataframe (used at the end), and all_movies dict (used in the main function)
    '''
    reader = pd.read_csv(file_name)
    movies = reader.values     
    all_movies = {movie[0]: (movie[2], movie[1], movie[3], movie[4], movie[11]) for movie in movies}
    
    # If interested to check what all_movies consists of.
    # count = 0
    # for key, value in all_movies.items():
    #     print(f'{key}: {value}')
    #     count += 1
    #     if count > 10: 
    #         break

    return reader, all_movies


def sanitizer(initial_str):
    '''
    Removes all capital letters.
    Removes all signs, symbols and punctuation that is not needed.
    Prepares a str to be used for searching.      

    Parameters
    ----------
    initial_str : str
        input

    Returns
    -------
    initial_str : str
        cleaned version of the initial str

    '''
    # make all letters lowercase
    initial_str = initial_str.lower()     
    # sanitize string (dispose of any punctuation, symbols, and others) 
    initial_str = initial_str.replace(",", " ").replace(";", " ").replace(":", " ").replace(".", " ").replace("!", " ").replace("(", " ").replace(")", " ").replace("\"", " ").replace("\'", " ").replace("\\", " ").replace("/", " ").replace("[", " ").replace("]", " ")
    # initial_str.strip()
    return initial_str


def get_show_str(show):
    '''
    Checks if the given str is meaningful. For instance, there is no nan.
    Composes a new string that consists of a movie title, cast, and description.
    This info will be used when building the index.
    
    Parameters
    ----------
    show : str
        info for the show

    Returns
    -------
    initial_str : str
        sanitized str with info for the show (title, cast, description)

    '''
    
    # check and add only meaningful strings (nan...don't work)
    if isinstance(show[0], str):
        title = show[0]
    else:
        title = ''
    if isinstance(show[1][3], str):
        cast = show[1][3]
    else:
        cast = ''
    if isinstance(show[1][4], str):
        description = show[1][4]
    else:
        description = ''
    
    # compose a string 
    initial_str = title + " " + cast + " " + description
    initial_str = sanitizer(initial_str)

    return initial_str

# Inspiration for creating a stemming algorithm: https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk
# Credit for helping build the index: https://www.datacamp.com/community/tutorials/stemming-lemmatization-python
def build_index(show_db):
    '''
    The actual index creation. This function uses PorterStemmer from the NLTK package 
    to extract only the root of the word.
    Example: "running", "runner" will be stemmed to just "run"
    Then, it builds an index dictionary with the stem as a key and the list of show IDs that
    contain the stem as part of the title, cast or description as values.

    Parameters
    ----------
    show_db : dict
        contains all_movies and their info as read by the file_reader()

    Returns
    -------
    index : dict
        dictionary with the word as a key and values are a list of all show IDs where the word was found

    '''
    ps = PorterStemmer() # for faster reference 

    # container (dictionary) to store the words with indexes
    index = {}
    # logic for filling the index container
    for show in show_db.items():
        info_str = get_show_str(show)
        info_str_set = set(map(ps.stem, info_str.split())) # to create a set of unique stems
        for word_tmp in info_str_set: # word_temp is the word that serves as a key
            if word_tmp not in index: # to check if the key already exists
                index[word_tmp] = []      
            index[word_tmp].append(show[0]) # to add the values
    
    # print(index) # to check the dictionary that is returned
    return index


def index_service(word):
    '''   
    The actual show search. Here, we use Natural Language Processing to make it easy for the user to find shows.
    The index_service() uses build_index() to find the show, where the specific word is found. 
    We could also search for a collocation or a non-sanitized word.
    The method will find out the shows in which all words are used (intersection).
    This helps out the user to narrow down the search.

    Parameters
    ----------
    word : str
        the word a user is looking for. It can be two words or more as well.
        The given word is stemmed and all punctuation and unnecessary symbols are removed.

    Prints
    -------
    If show info found: information for the show(s) (title, cast, description), retrieved using
    the word(s) the user have inputted
    
    If show info not found: error message
    
    Returns
    -------
    None (there is an option to return in the comments below)

    '''
    word = sanitizer(word) 
    words = word.split() # if a collocation is given we need to look for each word separately first
    stop_words = set(stopwords.words('english'))   # the build_index() gives us stop words as well but we would like to remove these when searching
    ps = PorterStemmer()
    
    words = map(ps.stem, words) # if we have words "beginning runner" => ["begin", "run"]

    show_db = file_reader('.\\data\\netflix_titles.csv')[1] # because the file_reader returns two elements and we want the dict
    
    index = build_index(show_db)

    
    # SEARCHING WORD
    # list containing sets in case of more than one word searched
    result = []
    # compiling the returned cotainer
    for word in words:
        if word not in stop_words:
            # creating a container for each individual term/word
            inner_result = []
            if word in index: # if word is in keys
                for show_idx in index[word]: # iterate over all values of a certain key in index
                    inner_result.append(show_db[show_idx]) # append show info extracted through finding the key in show_db
            if inner_result:
                result.append(set(inner_result)) # will add the show only once
    
    if not result:
        final_result = result # empty in case stop word is sought
        print(f"The word(s) \"{word}\" cannot be found or it is a stop word.")
    else:
        # If we give a collocation of words => find intersection of sets 
        # https://stackoverflow.com/questions/2541752/best-way-to-find-the-intersection-of-multiple-sets
        final_result = set.intersection(*result)
    
    for show in final_result:
        print()
        print(show)
    print()
    
    # return index             # this could be used for finding most common stems




def main():
    """
    Trying the functions. Possible Combinations: 
        # For only one movie, try: saadat
        # For a lot of movie results: beginning
        # For a collocation: tech expert evidence
        # For checking sanitizer: chess ? Anya!
        # For checking stop words: the
        
    Creates a plot with number of movies created each year.
    """
    query = input("Please enter search word: ")    
    index_service(query)
    
    # Showing a histogram of movies created each year. In 2018, there were the most movies created so far
    # Credit: https://www.statology.org/pandas-groupby-count/
    plt.figure(figsize=(15,13))
    data = file_reader('.\\data\\netflix_titles.csv')[0]
    data = data.groupby(['release_year'])['release_year'].count() # grouping by release year and counting the instances
    data.plot(kind = "bar", color=['#C986ED']) # this is the specific plot type and shade of purple I wanted to have on the plot



if __name__ == '__main__':
    main()








