movies = ["Terminator 2","Interstellar","Ant Man 2","3 Idiots"]
action = [1,0,1,0]
scifi = [1,1,1,0]
adventure = [0,1,1,0]
comedy = [0,0,1,1]
drama = [0,1,0,1]

df_item_features = pd.DataFrame({
    'movie':movies,
    'Action':action,
    'Sci-Fi':scifi,
    'Adventure':adventure,
    'Comedy':comedy,
    'Drama':drama
})

user = ['user 1','user 2','user 3','user 4']
terminator_2 = [7,8,9,0]
interstellar = [9,0,0,7]
ant_man_2 = [8,6,0,0]
three_idiots = [9,5,10,9]

df_user_items = pd.DataFrame({
    'user':user,
    'Terminator 2':terminator_2,
    'Interstellar':interstellar,
    'Ant Man 2':ant_man_2,
    '3 Idiots':three_idiots
})

movies = ["Titanic","Martian","GOTG Vol 2"]
action = [1,0,1]
scifi = [1,1,1]
adventure = [0,1,1]
comedy = [0,0,1]
drama = [0,1,0]

df_item_features_new = pd.DataFrame({
    'movie':movies,
    'Action':action,
    'Sci-Fi':scifi,
    'Adventure':adventure,
    'Comedy':comedy,
    'Drama':drama
})


def user_recommendation_multiple(df_user_items,df_item_features,df_item_features_new):
  
  arr_user_items = np.array(df_user_items.drop('user', axis = 1))
  arr_item_features = np.array(df_item_features.drop('movie', axis = 1))

  n_user = arr_user_items.shape[0]
  n_item = arr_user_items.shape[1]
  n_feature = arr_item_features.shape[1]

  arr_user_items_score = np.empty((n_user,n_item))
  arr_user_feature = np.empty((n_user,n_feature))

  for i in range(0,n_user):
    # print(arr_user_items[i,:])
    user_feature = np.matmul(arr_user_items[i,:],arr_item_features)
    # print(user_feature)
    user_feature = user_feature/user_feature.sum()
    arr_user_feature[i,:] = user_feature

  df_user_feature = pd.DataFrame(arr_user_feature)
  df_user_feature.columns = df_item_features.columns[1:]
  df_user_feature.index = user

  for i in range(0, n_user):
    user_item_score = np.matmul(arr_item_features,arr_user_feature[i,:])
    arr_user_items_score[i,:] = user_item_score

  arr_user_items_score_unwatched = np.where(arr_user_items == 0,arr_user_items_score,0)

  df_user_items_score_unwatched = pd.DataFrame(arr_user_items_score_unwatched)
  df_user_items_score_unwatched.columns = df_user_items.columns[1:]
  df_user_items_score_unwatched.index = df_user_items['user']

  arr_item_features_new = np.array(df_item_features_new.drop('movie', axis = 1))

  n_item_new = df_item_features_new.shape[0]

  arr_user_items_score_new = np.empty((n_user,n_item_new))

  for i in range(0, n_user):
    user_item_score = np.matmul(arr_item_features_new,arr_user_feature[i,:])
    arr_user_items_score_new[i,:] = user_item_score

  df_user_items_score_new = pd.DataFrame(arr_user_items_score_new)
  df_user_items_score_new.index = user
  df_user_items_score_new.columns = df_item_features_new['movie']

  return [df_user_items_score_unwatched,df_user_items_score_new]