import random


def flip_coin():
    """H: Head, T: Tail"""
    return random.choices(['H', 'T'])[0]


def play_game(games, cost_per_play, win_price):
    earning = 0
    """Win Condition: When coin flip would be Head"""
    for _ in range(games):
        if flip_coin() == 'H':
            earning += win_price
            earning -= cost_per_play
            print(f'Win / Balance: {earning} Tk')
        else:
            earning -= cost_per_play
            print(f'Lost / Balance: {earning} Tk')

    return earning


def main():
    game_count = int(input("Total games: "))
    cost_per_play = int(input("Cost per play: "))
    win_price = int(input("Win price: "))

    earning = play_game(game_count, cost_per_play, win_price)
    print(f"Total balance from {game_count} games are {earning} Tk")


if __name__ == '__main__':
    main()
