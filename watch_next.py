# Import spacy and load en_core_web_dm to perform semantic similarity operations
import spacy
nlp = spacy.load('en_core_web_md')

# Store movie description we want to compare 
hulk = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator'

# Read movies.txt into the variable movies
movies = open('movies.txt', 'r')

# Store a list of movie description strings. Strip new-line characters. Create a dictionary of movie names with their descriptions
movie_lines = movies.readlines()
movie_lines = [line.strip('\n') for line in movie_lines]

movie_dict = {line[:8]:line[9:-1] for line in movie_lines}

# Define function to compare the description of the movie watched to the list of potential recommendations
def watch_next(description):
    # Tokenise the original movie description
    description_token = nlp(description)
    # Compare each new movie with the watched movie description. Use the returned values as values in a new dictionary, retaining original keys
    results_dict = {key: nlp(value).similarity(description_token) for key, value in movie_dict.items()}

    # Return the key of the maximum value in the results dictionary
    movie_choice = max(results_dict, key=results_dict.get) 
    return f'Based on the last movie you watched, we recommend you try {movie_choice}\n\nHappy viewing!\n\n'

print(watch_next(hulk))

    
