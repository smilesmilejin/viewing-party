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
        for friends_watched in user_data['friends']:
            for each_friend_watched in friends_watched.values():
                if user_watched in each_friend_watched:
                    no_friend_has_watched = False
                    continue
        if no_friend_has_watched:
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

def get_available_recs(user_data):
    friends_watched_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)
    
    recommended_movies = []
    for movie in friends_watched_list:
        if movie not in user_data["watched"] and movie not in recommended_movies and movie["host"] in user_data["subscriptions"]:
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
    
    # Append the movie to the list if the user's friends have watched it, 
    # and if its genre matches the most popular genre, and the user hasn't seen it.
    for friends_watched in user_data['friends']:
        if not friends_watched['watched']:
            continue
        for each_friend_watched in friends_watched['watched']:
            if each_friend_watched['genre'] == most_popular_genre:
                user_not_watched = True
                for user_watched in user_data['watched']:
                    if user_watched['title'] == each_friend_watched['title']:
                        user_not_watched = False
                        break

                if ((user_not_watched) and 
                    (each_friend_watched not in rec_movies)
                    ):
                    rec_movies.append(each_friend_watched)
                
    return rec_movies

def get_rec_from_favorites(user_data):
    rec_movies=[]

    if (not user_data['favorites']) or (not user_data['watched']):
        return rec_movies
    if not user_data['friends']:
        rec_movies = user_data['favorites']
        return rec_movies

    for fav_movie in user_data['favorites']:
        friends_never_watched = True
        for friends_watched in user_data['friends']:
            for each_friend_watched in friends_watched['watched']:
                if each_friend_watched['title'] == fav_movie['title']:
                    friends_never_watched = False
                    break

        if friends_never_watched:
            rec_movies.append(fav_movie)

    return rec_movies