# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if (not title) or (not genre) or (not rating):
        return None
    movie_dict = {"title": title, "genre": genre, "rating": rating}
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0

    num_of_watched_movies = len(user_data["watched"])
    
    sum = 0
    for movie in user_data["watched"]:
        sum += movie["rating"]

    return sum / num_of_watched_movies

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    watched_genres_list = []
    for movie in user_data["watched"]:
        watched_genres_list.append(movie["genre"])

    watched_genres_dict = {}
    for genre in watched_genres_list:
        if genre not in watched_genres_dict:
            watched_genres_dict[genre] = 0
        watched_genres_dict[genre] += 1
    
    max_freq = 0
    max_genre = None
    for genre, freq in watched_genres_dict.items():
        if freq > max_freq:
            max_freq = freq
            max_genre = genre

    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_movies = []

    for user_watched in user_data['watched']:

        no_friend_has_watched = True
        for each_friend_watched in user_data['friends']:
            if user_watched in each_friend_watched['watched']:
                no_friend_has_watched = False
                break
        
        if no_friend_has_watched:
            unique_movies.append(user_watched)
    
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies= []

    for each_friend_watched in user_data['friends']:
        for each_movie in each_friend_watched['watched']:
            if (
            (each_movie not in user_data['watched']) and 
            (each_movie not in friends_unique_movies)
            ):
                friends_unique_movies.append(each_movie)
    
    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    friends_watched_list = get_friends_unique_watched(user_data)
    recommended_movies = []
    for movie in friends_watched_list:
        if movie not in recommended_movies and movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre (user_data):
    rec_movies = []
    if (not user_data) or (not user_data['watched']) :
        return rec_movies

    most_popular_genre = get_most_watched_genre(user_data)
    
    friends_watched = get_friends_unique_watched(user_data)

    for each_movie in friends_watched:
        if each_movie['genre'] == most_popular_genre and each_movie not in rec_movies:
            rec_movies.append(each_movie)
                
    return rec_movies

def get_rec_from_favorites(user_data):
    rec_movies=[]

    if (not user_data['favorites']) or (not user_data['watched']):
        return rec_movies
    if not user_data['friends']:
        rec_movies = user_data['favorites']
        return rec_movies

    user_watched = get_unique_watched(user_data)
    
    for movie in user_watched:
        if movie in user_data['favorites'] and movie not in rec_movies:
            rec_movies.append(movie)

    return rec_movies