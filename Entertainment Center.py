import fresh_tomatoes

import media

 #The purpose of this section is to initialize all values in the Movie Class for each movie in the Media Module

Gone_with_the_Wind = media.Movie("gone with the wind", "A story of the life of a civil war southern belle",
                                 "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Poster_-_Gone_With_the_Wind_01.jpg/440px-Poster_-_Gone_With_the_Wind_01.jpg",
                                 "https://youtu.be/0X94oZgJis4?t=13")
print (Gone_with_the_Wind.storyline)

forest_gump = media.Movie("forest gump", "A story of a simple man with low i.q.but good intentions", "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg","https://youtu.be/uPIEn0M8su0?t=4")


print (forest_gump.storyline)

titanic = media.Movie("titanic","A story of an american epic romance disaster and a shipwreck","https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                      "https://youtu.be/ZQ6klONCq4s?t=2")

print (titanic.storyline)

#"import fresh_tomatoes" turns this code into a movie website via the function "open_movies_page"
#"open_movies_page" extracts a list of movies and opens them up in an html webpage


movies = [Gone_with_the_Wind, forest_gump, titanic]

fresh_tomatoes.open_movies_page (movies)

                          
                          
                
