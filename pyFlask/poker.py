import random

def poker(player):
    PLAYER = player
    player_cards = {'Player_%s'%(i+1): list() for i in range(0,PLAYER)}

    # Generate 52 poker cards
    style_list = ['Spade', 'Heart', 'Diamond', 'Club']
    poker_list = ['%s_%s'%(style_list[int(i%4)], int(i/4) + 1) for i in range(0, 52)]

    # Shuffling
    random_poker_list = []
    while len(poker_list) > 0:
        choice = random.randint(0, len(poker_list)-1)
        random_poker_list.append(poker_list[choice])
        del poker_list[choice]

    # Distributing
    for n, c in enumerate(random_poker_list):
        player_cards['Player_%s' % (n % PLAYER + 1)].append(c)

    return player_cards

if __name__ == '__main__':
    player_cards = poker(5)

    # Order and print
    # for i in player_cards:
    #     player_cards[i].sort(key=lambda x: x.split('_')[0])
    #     print(i)
    #     print(player_cards[i])
    #     print()
    print(player_cards)