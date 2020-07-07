

import pandas as pd
from math import sqrt
import numpy as np

movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')
movies_df['year'] = movies_df.title.str.extract('(\(\d\d\d\d\))',expand=False)
movies_df['year'] = movies_df.year.str.extract('(\d\d\d\d)',expand=False)
movies_df['title'] = movies_df.title.str.replace('(\(\d\d\d\d\))', '')
movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())
movies_df['genres'] = movies_df.genres.str.split('|')
movies_df=movies_df[movies_df['year'].notna()]
movies_df['year']=movies_df['year'].astype('int')
movies_df=movies_df.loc[movies_df.year>1980]
moviesWithGenres_df = movies_df.copy()


for index, row in movies_df.iterrows():
    for genre in row['genres']:
        moviesWithGenres_df.at[index, genre] = 1

moviesWithGenres_df = moviesWithGenres_df.fillna(0)

ratings_df = ratings_df.drop('timestamp', 1)

def recommend(userInput):
	inputMovies = pd.DataFrame(userInput)
	inputId = movies_df[movies_df['title'].isin(inputMovies['title'].tolist())]
	inputMovies = pd.merge(inputId, inputMovies)
	inputMovies = inputMovies.drop('genres', 1).drop('year', 1)
	userMovies = moviesWithGenres_df[moviesWithGenres_df['movieId'].isin(inputMovies['movieId'].tolist())]
	userMovies = userMovies.reset_index(drop=True)
	userGenreTable = userMovies.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)
	userProfile = userGenreTable.transpose().dot(inputMovies['rating'])
	genreTable = moviesWithGenres_df.set_index(moviesWithGenres_df['movieId'])
	genreTable=genreTable.loc[~genreTable.movieId.isin(userMovies.movieId)]
	genreTable = genreTable.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)
	recommendationTable_df = ((genreTable*userProfile).sum(axis=1))/(userProfile.sum())
	recommendationTable_df = recommendationTable_df.sort_values(ascending=False)
	return list(movies_df.loc[movies_df['movieId'].isin(recommendationTable_df.head(5).keys()).tolist()].title)