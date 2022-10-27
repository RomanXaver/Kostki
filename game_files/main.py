'''
All relevant information can be found in the README.md
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
