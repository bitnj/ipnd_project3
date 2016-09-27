import media
import fresh_tomatoes


# hard-coded movie information
young_frankenstein = media.Movie("Young Frankenstein", """Respected medical
    lecturer Dr. Frederick Frankenstein (Gene Wilder) learns that he has
    inherited his infamous grandfather's estate in Transylvania. Arriving at the
    castle, Dr. Frankenstein soon begins to recreate his grandfather's
    experiments with the help of servants Igor (Marty Feldman), Inga (Teri Garr)
    and the fearsome Frau Blucher (Cloris Leachman). After he creates his own
    monster (Peter Boyle), new complications ensue with the arrival of the
    doctor's fiancee, Elizabeth (Madeline Kahn).""", 105, "Comedy", 1974, 
    "https://upload.wikimedia.org/wikipedia/en/b/b5/Young_Frankenstein_movie_poster.jpg",
    "https://www.youtube.com/watch?v=mOPTriLG5cU")

caddy_shack = media.Movie("Caddy Shack", """Danny Noonan (Michael O'Keefe), a
    teen down on his luck, works as a caddy at the snob-infested Bushwood
    Country Club to raise money for his college education. In an attempt to gain
    votes for a college scholarship reserved for caddies, Noonan volunteers to
    caddy for a prominent and influential club member (Ted Knight). Meanwhile,
    Danny struggles to prepare for the high pressure Caddy Day golf tournament
    while absorbing New Age advice from wealthy golf guru Ty Webb
    (Chevy Chase).""", 98, "Comedy", 1980,
    "https://upload.wikimedia.org/wikipedia/en/8/84/Caddyshack_poster.jpg",
    "https://www.youtube.com/watch?v=zrTqenN1SqQ")

raiders_lost_ark = media.Movie("Raiders of the Lost Arc", """Archaeologist and
    adventurer Indiana Jones is hired by the U.S. government to find the Ark
    of the Covenant before the Nazis.""", 105, "Action/Adventure", 1981,
    "https://upload.wikimedia.org/wikipedia/en/4/4c/Raiders_of_the_Lost_Ark.jpg",
    "hhttps://www.youtube.com/watch?v=XkkzKHCx154")

the_game = media.Movie("The Game", """Nicholas Van Orton is a very wealthy San
    Francisco banker, but he is an absolute loner, even spending his birthday
    alone.  In the year of his 48th birthday (the age his father committed
    suicide) his brother Conrad, who has gone long ago and surrendered to
    addictions of all kinds, suddenly returns and gives Nicholas a card giving
    him entry to unusual entertainment provided by something called Consumer
    Recreation Services (CRS). Giving in to curiosity, Nicholas visits CRS and
    all kinds of weird and bad things start to happen to him""", 128,
    "Thriller", 1997,
    "https://upload.wikimedia.org/wikipedia/en/5/53/TheGame_poster323.jpg",
    "https://www.youtube.com/watch?v=0kqQNBR09Rc")

the_ref = media.Movie("The Ref", """A cat burglar is forced to take a bickering,
    dysfunctional family hostage on Christmas Eve.""", 96, "Comedy", 1994,
        "https://upload.wikimedia.org/wikipedia/en/3/3a/Ref_ver1.jpg",
        "https://www.youtube.com/watch?v=_26ROmuSyTQ")

# put Movie objects in a list that can be passed to
# fresh_tomatoes.open_movies_page
movies = [young_frankenstein, caddy_shack, raiders_lost_ark, the_game, the_ref]

# generates and opens a web page that displays the movies
fresh_tomatoes.open_movies_page(movies)


