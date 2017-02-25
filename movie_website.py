import media # Importing media for Movie class
import fresh_tomatoes # Importing functions from fresh_tomatoes.py

# Instantiating multiple instances of the object movie
shawshank = media.Movie("Shawshank Redemption", \
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", \
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

forrest_gump = media.Movie("Forrest Gump", \
                          "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg", \
                          "https://www.youtube.com/watch?v=8dcYw4OwCA0")

inception = media.Movie("Inception", \
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", \
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

inside_out = media.Movie("Inside Out", \
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg", \
                         "https://www.youtube.com/watch?v=yRUAzGQ3nSY")

lala_land = media.Movie("La La Land", \
                        "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png", \
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")

braveheart = media.Movie("Braveheart", \
                         "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg", \
                         "https://www.youtube.com/watch?v=wj0I8xVTV18")

beautiful_mind = media.Movie("A Beautiful Mind", \
                             "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg", \
                             "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

gladiator = media.Movie("Gladiator", \
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg", \
                        "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

# Concatenating Movie objects into list
movie_list = [shawshank, forrest_gump, inception, inside_out, lala_land, braveheart, beautiful_mind, gladiator]

# Calling the open_movies_page in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movie_list)