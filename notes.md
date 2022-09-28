Classes: Rock, Paper, Scissors, Lizard, Spock, Game(parent)

scissors & lizard "does" beat paper
paper & spock "does" beat rock
rock & scissors "does" beat lizard
lizard & paper "does" beat spock
spock & rock "does" beat scissors

class group1 "has" scissors & lizard
class group2 "has" paper & rock
class group3 "has" rock & scissors
class group4 "has" lizard & paper
class group5 "has" spock & rock 



Display name of game 
Display # of players
    display names of players
    display game type between player vs AI or player vs player
    display turn of player
Display Rules of game:
    display available options-[Rock, Paper, Scissors, Lizard, Spock] for each game round 
    display what each option-[Rock, Paper, Scissors, Lizard, Spock] wins or loses against for each game round 
    display player chosen choice
        if the choice is invalid, display the game options-[] again for player to choose again
    display game round results based off of player chosen choice
        display count of rounds won per player
    display winner after 2 wins
    display loser after 2 losses
