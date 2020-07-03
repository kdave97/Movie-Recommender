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







