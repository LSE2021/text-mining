# text-mining

Natural Language Processing Project of Netflix
by Martina Garabedian

Credits given to all resources used in main program.

One of the most prominent features of modern search engines is that people do not have to know what they are exactly looking for. Just simply typing a key word should enable the search engine to find the desired result. Netflix also offers such search and in this project I built a "smarter" search engine which is able to look for a movie (in our netflix_titles.csv dataset) using one or multiple key words and return the show(s) information - title, type, director, cast, description. The code could be found in stemming_search.py.

To achieve this I used the Python NLTK package and more specifically the PorterStemmer. This module allowed me to get the stem of each word that the user inputs. For instance, if the user inputs "beginning" or "beginner", the PorterStemmer will help me get just "begin" and that way I could look through all shows that contain words with the root "begin". I also used the stopwords from NLTK to clean all words such as "the", "which" and many more, which appear in any movie information and would not give the user any meaningful information. 

The other packages I used are pandas and matplotlib. The netflix_titles.csv file from Kaggle consists of 8807 unique observations about a movie and its information (https://www.kaggle.com/datasets/shivamb/netflix-shows). Pandas helped me read the initial .csv file as a dataframe before converting it in the all_movies dictionary. This dataframe was later on used in plotting using matplotlib. From all the information given in the dataset I decided to use the title, type of movie, director, cast, and description.

In the implementation phase, I created 5 functions plus the main() and if __name__ functions. 

Please refer to the highly detailed docstrings and comments in stemming_search.py for more information about each step.

The general steps and decisions in building the program were as follows:
1. Read the file and create a dataframe for plots and pandas analysis. Create also a dictionary that will be searched.
2. I cleaned the data by converting everything into lowercase and removing all punctuation at the front or back of the words. This is needed because it helps the search later on when we compare the user's input and what we have in our dataset. In sanitizing the string, I decided to use chaining in order to use the object reference just once to remove all punctuation, symbols, and other troublesome signs.
3. Then I created a string with only the titles, cast, and descriptions that are meaningful and in string format. 
4. The bread and butter of the program are the build_index(show_db) and index_service(word) functions. The algorithm behind building the index is responding to the fact that we need to know in which shows does each stem appear. So a dictionary of the stem and then a list of the show IDs that this stem appears in was the way to search the dataset. 
Example of index => 'aliza': ['s764', 's1737']
5. Then in index_service was the actual show search using NLTK. Here, I decided to make the program more sophisticated by being able to search even if more than one word is searched. The most complicated part was to be able to make the program to look for intersection of sets if we give a collocation. Thankfully, StackOverflow had some suggestions. Please, see examples in the Result section.

While the steps above describe multiple decisions made throughout the implementation stage. One decision that I believe was critical to the operations was the container I use to store the .csv dataset. I first tried working with list of lists but this turned out inefficient because the program was very slow when reading and then it would have been harder to refer to specific shows. Therefore, I chose to use a dictionary for all_movies and return the value when a stem is found. This works faster and better. 

Results

The program asks for input from the user in the console. If a word or a collocation is given, then the program searches the word in index, finds all the shows IDs that contain it, searches by the show ID (which is a key in show_db) and it prints the movie information taken from show_db value. 

Here are some examples of how it operates.
1. If you input "saadat"
('Manto', 'Movie', 'Nandita Das', 'Nawazuddin Siddiqui, Rasika Dugal, Tahir Raj Bhasin', 'The controversial and troubled Indo-Pakistani writer Saadat Hasan Manto finds his artistic choices challenged by censors.')

2. If you input "hetfield"
('Metallica: Some Kind of Monster', 'TV Show', 'Joe Berlinger, Bruce Sinofsky', 'James Hetfield, Lars Ulrich, Kirk Hammett, Robert Trujillo', 'This collection includes the acclaimed rock documentary about Metallica, plus a film checking in with the still-thriving group 10 years later.')

('Metallica Through The Never', 'Movie', 'Nimród Antal', 'Dane DeHaan, James Hetfield, Lars Ulrich, Kirk Hammett, Robert Trujillo', 'As heavy metal band Metallica tears up the stage, a young roadie is sent on an urgent errand. But his mission soon takes a surreal turn.')

3. If you input a collocation "tech expert evidence"
('Master', 'Movie', 'Ui-seok Jo', 'Byung-hun Lee, Dong-won Gang, Woo-bin Kim, Ji-won Uhm, Dal-su Oh, Kyung Jin, Gang Dong-won', "Needing hard evidence to convict a company chairman of fraud, an investigator bargains with the company's tech expert to turn over his boss's ledger.")

4. If you input a collocation which is not sanitized like "chess ? Anya!"
("The Queen's Gambit", 'TV Show', nan, 'Anya Taylor-Joy, Bill Camp, Marielle Heller, Thomas Brodie-Sangster, Moses Ingram, Harry Melling, Isla Johnston, Christiane Seidel, Rebecca Root, Chloe Pirrie, Jacob Fortune-Lloyd', 'In a 1950s orphanage, a young girl reveals an astonishing talent for chess and begins an unlikely journey to stardom while grappling with addiction.')

In addition, I made use of Pandas as mentioned earlier.

Here, is an image of the histogram showing all movies created each year. In 2018, there were the most movies created so far. I made the graph purple because I love this color. 

![Netflix Movies Created by Year](Figure_1.png) # I found this code online but not sure if it will properly show the figure in .md. If not, please find it in the images folder.

Reflection

I think that the program is working very well and it is optimized to the maximum. However, the NLTK package really slows it down and it takes a couple of seconds to get the show information. In the real world, there will not be as much of a wait so I welcome suggestions on how to make the program faster. This was a very deep dive in one of the options for the project (NLP) and I also added the graph to make it more interactive. Going forward, I am more interested in exploring the statistical options through Pandas using this dataset. 