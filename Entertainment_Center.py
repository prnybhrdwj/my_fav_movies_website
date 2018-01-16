import media
import fresh_tomatoes

#We will create individual instances of all movies by using class constructor
toy_story = media.Movie(
        "Movie", "Toy story",
        "A story of a boy and his toys that come to life",
        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie(
        "Movie", "Avatar",
        "A marine on an alient planet trying to save the natives",
        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
        "https://www.youtube.com/watch?v=d1_JBMrrYw8")

coco = media.Movie(
        "Movie", "Coco",
        "Young boy goes to land of the dead and discovers secrets about his family's past.",
        "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
        "https://www.youtube.com/watch?v=zNCz4mQzfEI")

casablanca = media.Movie(
        "Movie", "Casablanca",
        "A bar owner in Casablanca helps his old lover flee to USA with her husband who is being chased by Nazi Germans.",
        "https://www.movieposter.com/posters/archive/main/2/b70-1191",
        "https://www.youtube.com/watch?v=BZtWRRa_8I0")

rashomon = media.Movie(
        "Movie", "Rashomon",
        "A heinous crime and its aftermath are recalled from differing points of view.",
        "https://i.pinimg.com/originals/92/1d/2d/921d2d8552f85c25bf9307f0d02b7c6b.jpg",
        "https://www.youtube.com/watch?v=xCZ9TguVOIA")

its_a_wonderful_life = media.Movie(
        "Movie", "It's a wonderful life",
        "An angel helps a desperately frustrated businessman by showing him what life would be without him.",
        "https://images-na.ssl-images-amazon.com/images/I/5164PhRtw2L.jpg",
        "https://www.youtube.com/watch?v=ewe4lg8zTYA")

#We will create a list called movies and keep every movie instance inside it
movies = [toy_story, avatar, coco, casablanca, rashomon, its_a_wonderful_life]

#Since open_movies_page accepts a list as an input, we will use our movies list
fresh_tomatoes.open_movies_page(movies)
