'''
Welcome to the game "Kostki"!
The way you play the game is pretty simple:

In the beginning you roll your dice and try to collect points.

The points are counted as following:
Only 1 and 5 can be picked up separately. 1 = 100 points and 5 = 50 points
3x 2 = 200 points (3x 3 = 300 and so forth) except for 3x 1 which is 1000
6x 2 = 2000 points (3x 3 = 300 and so forth) except for 6x 1 which is 10000

Phase 1:
In the first phase every player first needs to reach at least 1050 points or more, in order to reach the phase two

Phase 2:
In the second phase of the game every player can write down any points number if its at least 350 points.

Phase 3:
As soon as the first player hits 10050 points, every player coming after him still gets one try. So if your turn was
before the players who hit 10050, that is bad luck. This is also the reason why you always want to be the last person to
throw your dice. In the end the player wins who has the most points.
'''

def initialize_player():

    print("Welcome to Kostki!!!")
    # Ask how many players are in the game
    while True:
        try:
            p_count = int(input("\nNumber of players playing the game?: "))
            break
        except ValueError:
            print("\nPlease enter a valid number!")

    player_list = []
    # asking for the players names
    for i in range(p_count):
        player_name = input("\nWhat is the name of player " + str(i + 1) + "? ")
        player_list.append(player_name)

    # creating the dictionary, with the players and their points
    points = [0] * p_count
    initialize_player.d = {player: points for player, points in zip(player_list, points)}

    print("\n")

# creating function
def play_round(current_round=1):

    if current_round == 1:
        initialize_player()

    for player in initialize_player.d.keys():
        points_round = int(input("Points for " + str(player) + " in round " + str(current_round) + ": "))
        initialize_player.d[player] += points_round
    print(initialize_player.d)
    for player, points in initialize_player.d.items():
        if points >= 10050:
            winning_player = max(initialize_player.d, key=initialize_player.d.get)
            print(winning_player, "Is the Winner!!!")
            raise SystemExit("The game is over!")
        else:
            play_round(current_round + 1)


play_round()
