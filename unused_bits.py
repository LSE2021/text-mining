# This file contains some stuff I have tried but they didn't work. Please disregard it. 


#---------------------------------------------------------------
######## Create a dictionary from netflix_titles.csv file

# netflix_dict = {}
# for i in range(len(netflix[0])): # Assuming that there are no NA cells
#     dict_key = netflix[0][i] # Taking first list as the keys
#     if dict_key in netflix_dict:
#         raise KeyError("The key already exists!")
#     netflix_dict[dict_key] = []
#     for row in range(1, len(netflix)): # Skips the first list with keys
#         netflix_dict[dict_key].append(netflix[row][i]) # To add a movie in the dict

# for key, value in netflix_dict.items():
#     print(f'{key}: {value[0]}')
#----------------------------------------------------------------

#----------------------------------------------------------------
# Create a pickle file for reading the .csv
# netflix_p = netflix.to_pickle('C:\Users\Student\Documents\Senior Year\OIM3640 - Python\text-mining\data\netflix_titles.pkl')    #to save the dataframe, df to 123.pkl
# print(netflix_p)
#----------------------------------------------------------------
# Open .csv file
# Creates a list with each movie as a nested list
# Order: ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']
# with open(r'C:\Users\Student\Documents\Senior Year\OIM3640 - Python\text-mining\data\netflix_titles.csv', newline='',  encoding='utf-8') as f:
#     reader = csv.reader(f)
#     netflix = list(reader)
# # print(netflix[0]) # Order