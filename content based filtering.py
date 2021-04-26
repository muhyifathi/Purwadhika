import pandas as pd
import numpy as np

movies = ["Terminator 2","Interstellar","Ant Man 2","3 Idiots"]
scores = [7,9,8,9]
action = [1,0,1,0]
scifi = [1,1,1,0]
adventure = [0,1,1,0]
comedy = [0,0,1,1]
drama = [0,1,0,1]

df_movies = pd.DataFrame({
    'movie':movies,
    'scores':scores,
    'Action':action,
    'Sci-Fi':scifi,
    'Adventure':adventure,
    'Comedy':comedy,
    'Drama':drama
})

movies = ["Titanic",'Martian','GOTG Vol 2']
action = [1,0,1]
scifi = [1,1,1]
adventure = [0,1,1]
comedy = [0,0,1]
drama = [0,1,0]

df_movies_recommendation = pd.DataFrame({
    'movie':movies,
    'Action':action,
    'Sci-Fi':scifi,
    'Adventure':adventure,
    'Comedy':comedy,
    'Drama':drama
})

def user_recommendation(df_movies,df_movies_recommendation):
  df_movies2 = df_movies.copy()
  df_movies2.drop('movie', axis = 1, inplace = True)

  for i in df_movies.columns[2:]:
    df_movies2[i] = df_movies2['scores']*df_movies2[i] 

  df_movies2.drop('scores', axis = 1, inplace = True)
  movie_scoring = df_movies2.sum()/df_movies2.sum().sum()

  for i in df_movies.columns[2:]:
    df_movies_recommendation[i] = df_movies_recommendation[i]*movie_scoring[i]

  df_movies_recommendation['movie rating prediction'] = df_movies_recommendation.sum(axis = 1)
  return df_movies_recommendation[['movie','movie rating prediction']]