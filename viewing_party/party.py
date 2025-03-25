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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_movies = []
    for user_watched in user_data['watched']:
        user_has_watched = True
        for friends_watched in user_data['friends']:
            for each_friend_watched in friends_watched.values():
                if user_watched in each_friend_watched:
                    user_has_watched = False
                    continue
        if user_has_watched:
            unique_movies.append(user_watched)
    return unique_movies

def get_friends_unique_watched(user_data):

    friends_unique_movies= []
    for friends_watched in user_data['friends']:
        for each_friend_watched in friends_watched.values():
            for each_movie in each_friend_watched:
                if (
                (each_movie not in user_data['watched']) and 
                (each_movie not in friends_unique_movies)
                ):
                    friends_unique_movies.append(each_movie)
    return friends_unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    # return [{'genre': 'Fantasy', 'host': 'hulu', 'rating': 4.0, 'title': 'The Programmer: An Unexpected Stack Trace'}]
    pass