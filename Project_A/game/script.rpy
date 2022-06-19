# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

define Red = Character("Red", color="#FF0000")
#image movie = Movie(channel="movie", play="movies/test.mkv")

label start:

    play sound "audio/Role.mp3" volume 0.5
    #scene bg "caff"
    show red idle
    play music "audio/Among_Us.mp3" fadein 1.0 volume 0.5
    Red "Among us, Among us, Among us, Among us, Among us"
    Red "Among us, Among us, Among us, Among us, Among us, Among us, Among us, Among us"
    Red "Among us, Among us, Among us, Among us"
    Red "Among us, Among us, Among us, Among us, Among us, Among us, Among us, Among us, Among us, Among us"
    Red "Among us"
    stop music fadeout 1.0
    #play sound "audio/SUS.mp3" volume 0.5

menu:
    "SUS":
        jump choice_a
    "Among Us":
        jump choice_b

label choice_a:
    play sound "audio/Errape.mp3" volume 10.0
    jump common

label choice_b:
    $ renpy.movie_cutscene("movies/yellow_dance.webm")
    play music "audio/found.mp3" volume 0.5
    jump common

label common:
    return

