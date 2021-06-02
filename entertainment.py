import media
import fresh_tomatoes
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=rNk1Wi8SvNc")
avatar = media.Movie("Avatar", "A marine on an alien plante", "https://static.miraheze.org/greatestmovieswiki/1/1c/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw%40%40._V1_.jpg", "https://www.youtube.com/watch?v=6ziBFh3V1aM")
school_of_rock = media.Movie("School of Rock", "Using rock music to learn", "https://static.miraheze.org/greatestmovieswiki/a/a8/220px-School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=TExoc0MG4I4")
ratatouille = media.Movie("Ratatouille", "Arat is a chef in Paris", "https://static.miraheze.org/greatestmovieswiki/1/1b/51MJQKcJVFL._SY450_.jpg", "https://www.youtube.com/watch?v=NgsQ8mVkN8w")
midnight_in_Paris = media.Movie("Midnight in Paris", "Going back in time to meet authors", "https://upload.wikimedia.org/wikipedia/commons/a/ac/Eiffel_Tower_at_Night_%285381700444%29.jpg", "https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games = media.Movie("Hunger Games", "A really real reality show", "https://upload.wikimedia.org/wikipedia/commons/9/98/The_hunger_games_mockingjay_part_2.svg", "https://www.youtube.com/watch?v=mfmrPu43DF8")


movies = [toy_story, avatar, school_of_rock,ratatouille , midnight_in_Paris, hunger_games]


fresh_tomatoes.open_movies_page(movies)
#print(toy_story.storyline)
#print(avatar.storyline)

#avatar.show_trailer()
