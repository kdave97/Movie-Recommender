# Movie-Recommender

## Project Description
The preoject involves building a movie recommender system. There are two types of filtering techniques i.e Content Based and Collaborative based Filtering system used in Recommender System. The project involves building both the models and deploying them on AWS using Flask web framework.

## DATASET
The Dataset is collected from Grouplens which has collected and made available rating datasets from [MovieLens](http://movielens.org), a movie recommendation service. This dataset (ml-latest) describes 5-star rating and free-text tagging activity which contains 22884377 ratings across 34208 movies. These data were created by 247753 users between January 09, 1995 and January 29, 2016.

The data are contained in four files, `links.csv`, `movies.csv`, `ratings.csv` and `tags.csv`. However for this project, we will be using only 'movies.csv' and 'ratings.csv'.

Movies.csv - movieId, title and genres. It consists of 34,208 movies.
Ratings.csv - userId, movieId, rating and timestamp - It consists of total of 22884377 ratings.

Download the above csv files from https://drive.google.com/file/d/1Gu2NgMi5ta5JfrJiSfbMQRC9LZSb9Xos/view?usp=sharing. Check out other datasets at https://grouplens.org/datasets/movielens/. To understand more about dataset, read the Dataset-info.txt. 

## Recommender Model
There are two techniques used in recommendation systems i.e Content-based Filtering techniques and Collaborative based Filtering techniques.

### Content-Based Recommender Model
A content-based recommender works on the principle of user's profile. Based on the ratings given by the user for the movies, the recommender model creates a user profile. It suggests movies to the user based on the user profile. The recommendation process is based on the similarity of the items. For eg: If a user rates high for a particular genre, the user profile will have high weightage for that genre and so it will suggest new movies of that genre. Recommendation is totally based on the taste and preferences of the user.

To get recommendations, following steps were performed:

* Preprocessing of the dataset involving handling missing values and data transformations.
* Generating a list of genres so as to simplify the recommendation process.
* Generating one-hot encoding matrix based on the different genres for each movie.
* Based on the user's interest, build a user profile.
* Get top 5 movies based on the highest scores.


### Collaborative-Based Recommender Model 
A collaborative based recommender model works on the principle of taking in account of other user's opinions and preferences based on user's interests. It attempts to find users that have similar preferences and opinions as the input and then recommends items that they have liked to the input. For eg: A user gives high rating to a particular movie. It finds the users who have similar kind of opinions as user and suggest movies based on his interests. Basically, it means if You like what I like the I may like what you like. 

To get recommendations, following steps were performed:

* Preprocessing of the dataset involving handling missing values and data transformations.
* Select a user with the movies the user has watched
* Based on his rating to movies, find the top 100 neighbours
* Get the watched movie record of the user for each neighbour.
* Calculate a similarity score using some formula
* Recommend top 5 items with the highest score


