# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if (not title) or (not genre) or (not rating):
        return None
    movie_dict = {"title": title, "genre": genre, "rating": rating}
    return movie_dict

def add_to_watched(user_data, movie):
    if movie in user_data["watched"]:
        return user_data
    
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    if movie in user_data["watchlist"]:
        return user_data
    
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0

    total = sum(movie["rating"] for movie in user_data["watched"])
    average_rating = total / len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    watched_genres_dict = {}
    for movie in user_data["watched"]:
        if movie['genre'] not in watched_genres_dict:
            watched_genres_dict[movie['genre']] = 0
        watched_genres_dict[movie['genre']] += 1

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
    friend_movie_titles = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movie_titles.add(movie["title"])

    unique_movies = []
    for movie in user_data["watched"]:
        if movie["title"] not in friend_movie_titles:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies= []

    for each_friend_watched in user_data['friends']:
        for each_movie in each_friend_watched['watched']:
            if ((each_movie not in user_data['watched'])
                    and (each_movie not in friends_unique_movies)):
                friends_unique_movies.append(each_movie)
    
    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    friends_watched_list = get_friends_unique_watched(user_data)
    
    recommended_movies = []
    for movie in friends_watched_list:
        if movie["host"] in user_data["subscriptions"]:
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
        if each_movie['genre'] == most_popular_genre:
            rec_movies.append(each_movie)
                
    return rec_movies

def get_rec_from_favorites(user_data):
    rec_movies=[]

    if (not user_data['favorites']) or (not user_data['watched']):
        return rec_movies
    
    # If the user does not have any friends, return the user's favorite movies
    if not user_data['friends']:
        rec_movies = user_data['favorites']
        return rec_movies

    user_watched = get_unique_watched(user_data)
    
    for movie in user_watched:
        if movie in user_data['favorites']:
            rec_movies.append(movie)

    return rec_movies