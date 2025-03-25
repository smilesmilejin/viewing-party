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

def get_new_rec_by_genre (user_data):

    rec_movies = []
    if (not user_data) or (not user_data['watched']) :
        return rec_movies
    genre_frequency = {}
    # Create a dictionary that maps each genre to its frequency.
    for each_movie in user_data['watched']:
        print(each_movie['genre'])
        if each_movie['genre'] not in genre_frequency:
            genre_frequency[each_movie['genre']] = 1
            continue
        genre_frequency[each_movie['genre']] += 1

    # Find the user's most frequent genres; if there's a tie, choose the first one.
    first_time = True
    for genre, score in genre_frequency.items():
        if first_time:
            max_score = score
            most_popular_genre = genre
            first_time = False
            continue

        if score > max_score:
            most_popular_genre = genre

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