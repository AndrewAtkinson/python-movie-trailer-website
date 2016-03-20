import media
import fresh_tomatoes

#initiate our movie classes
batman_vs_superman = media.Movie("Batman Vs Superman",
                                 "Fearing the actions of Superman are left unchecked, Batman takes on the man of steel, while the world wrestles with what kind of a hero it really needs. With Batman and Superman fighting each other, a new threat, Doomsday, is created by Lex Luthor. It's up to Superman and Batman to set aside their differences along with Wonder Woman to stop Lex Luthor and Doomsday from destroying Metropolis.",
                                 "http://ia.media-imdb.com/images/M/MV5BNTE5NzU3MTYzOF5BMl5BanBnXkFtZTgwNTM5NjQxODE@._V1_UY268_CR0,0,182,268_AL_.jpg",
                                 "yViIi3gie2c"
                                 )

the_departed = media.Movie("The Departed",
                            "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
                            "http://vignette2.wikia.nocookie.net/cinemorgue/images/b/b4/RrfDNbN.jpg/revision/latest?cb=20150519173826",
                            "auYbpnEwBBg",
                           "01/01/2010"
                           )

shutter_island = media.Movie("Shutter Island",
                            "A U.S Marshal investigates the disappearance of a murderess who escaped from a hospital for the criminally insane.",
                            "http://ia.media-imdb.com/images/M/MV5BMTMxMTIyNzMxMV5BMl5BanBnXkFtZTcwOTc4OTI3Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                            "5iaYLCiq5RM",
                             "10/08/1998"
                             )

inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",
                        "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "66TuSJo4dZM",
                        "16/08/2014"
                        )

dark_knight = media.Movie("The Dark Knight",
                        "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                        "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "EXeTwQWrcwY"
                          )

dark_knight_rises = media.Movie("The Dark Knight Rises",
                                 "Eight years after the Joker's reign of anarchy, the Dark Knight, with the help of the enigmatic Selina, is forced from his imposed exile to save Gotham City, now on the edge of total annihilation, from the brutal guerrilla terrorist Bane.",
                                 "http://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                 "GokKUqLcvD8"
                                )
#create list of movie objects
movies = [batman_vs_superman, the_departed, shutter_island, inception, dark_knight, dark_knight_rises]
#pass objects to open movies page function to generate html output
fresh_tomatoes.open_movies_page(movies)
