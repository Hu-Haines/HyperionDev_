'''  ***Practical Task 2: 
        building a movie recommendation system based on word vector similarity of descriptions  ***   '''

# imports
import spacy
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
nlp=spacy.load('en_core_web_md')

''' preprocessing functions'''
# tokenization function
def tokenization(text):
    doc = nlp(text)
    return ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])

# function for getting vectors for preprocessed texts
def get_vector(text):
    doc = nlp(text)
    return doc.vector


''' preprocessing the movie file '''
# loading in the movies file
movies = pd.read_csv('movies.txt', delimiter=":", header=None, names=['Movie', 'Description'])

# applying tokenization and get_vector functions and saving the information into a new column
movies['processed_description']= movies['Description'].apply(tokenization)
movies['vectors'] = movies['processed_description'].apply(get_vector)


''' recommendation function'''
# takes in description as a parameter and return the title of the most similar movie
# (this function has already encorperated the "movies.txt" movie dictionary, where it will pull out the recommendations)
def recommendation(input_description):
    # getting the vector and preprocessing for the input desciption
    input_vector = get_vector(tokenization(input_description)).reshape(1,-1)

    # calculating the cosine similarity
    similarity_scores = cosine_similarity(input_vector, list(movies['vectors']))
    
    # finding the highest similarity score and loacting it's index
    max_score = similarity_scores.max()
    max_score_index = np.where(similarity_scores[0] == max_score)

    # retreving the title of the highest similarity score movie
    recommended_titles = movies['Movie'].loc[max_score_index].tolist()
    return recommended_titles


''' applying the recommendation function with user's movie desciption'''
# user's variable: the movie user has watched
users_movie = {"Planet Hulk" : "Will he save their world or destory it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."}

# finding a movie recommendation from what user has watched
user_recommendation = recommendation(users_movie["Planet Hulk"])
print(f"If you liked {list(users_movie.keys())[0]}, I recommend you to watch {user_recommendation[0]}!")