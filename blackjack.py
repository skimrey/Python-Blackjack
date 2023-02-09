import random

i = 0 
deck = ['Club 1', 'Club 2', 'Club 3', 'Club 4', 'Club 5', 'Club 6', 'Club 7', 
       'Club 8', 'Club 9', 'Club 10', 'Club-Jack 10', 'Club-Queen 10', 'Club-King 10', 'Heart 1', 
        'Heart 2', 'Heart 3', 'Heart 4', 'Heart 5', 'Heart 6', 'Heart 7', 
        'Heart 8', 'Heart 9', 'Heart 10', 'Heart-Jack 10', 'Heart-Queen 10', 'Heart-King 10',
        'Diamond 1', 'Diamond 2', 'Diamond 3', 'Diamond 4', 'Diamond 5', 
        'Diamond 6', 'Diamond 7', 'Diamond 8', 'Diamond 9', 'Diamond 10', 
        'Diamond-Jack 10', 'Diamond-King 10', 'Diamond-Queen 10', 'Spade 1', 'Spade 2', 'Spade 3', 
        'Spade 4', 'Spade 5', 'Spade 6', 'Spade 7', 'Spade 8', 'Spade 9', 
        'Spade 10', 'Spade-Jack 10', 'Spade-Queen 10', 'Spade-King 10']


def Blackjack():
    
    dealer = []
    player = []
    playerscore = 0
    dealerscore = 0

    def Shuffle():
        random.shuffle(deck)
        
    def Deal():
        card1 = deck.pop()
        card2 = deck.pop()
        dealer1 = deck.pop()
        dealer2 = deck.pop()
        player.append(card1)
        player.append(card2)
        dealer.append(dealer1)
        playerscore = 0
        num = player[0].index(' ')
        num1 = player[1].index(' ')
        playerscore +=  int(player[0][num::]) + int(player[1][num1::])
        print(f'Player {player} {playerscore}')
        print(f'Dealer {dealer}')
        dealer.append(dealer2)
        
    def Hit():
        card1 = deck.pop()
        player.append(card1)
        playerscore = 0
        for m in range(len(player)):
            num = player[m].index(' ')
            playerscore +=  int(player[m][num::])
        print(f'Player {player} {playerscore}')
        return playerscore
    
    def Stay():
        for i in range(random.randrange(1, 3)):
            dealer1 = deck.pop()
            dealer.append(dealer1)
            dealerscore = 0
        for m in range(len(dealer)):
            num = dealer[m].index(' ')
            dealerscore +=  int(dealer[m][num::])
            if dealerscore > 21:
                print(f'Dealer {dealer} {dealerscore}')
                print('Dealer Bust: You Win')
                i = 1
                break
            elif dealerscore > 16:
                print(f'Dealer {dealer} {dealerscore}')
                break
            elif m == len(dealer):
                print(f'Dealer {dealer} {dealerscore}')
        return dealerscore

    def Play():
        Deal()
        x = 1
        a = playerscore
        b = dealerscore
        while x == 1:
            hit = input('hit or stay or quit')

            if hit ==  'hit':
                a = Hit()
                if a > 21:
                    x = 0
                    print('Bust')
                elif a == 21:
                    Stay()
            elif hit == 'stay':
                b = Stay()
                if b > 21:
                    x = 0
                if a < b and x == 1 and i == 0:
                    print('You Lose')
                    x = 0
                elif a > b and x == 1:
                    print(f'Dealer {dealer} {b}')
                    print('You Win')
                    x = 0
                elif a == b:
                    print('Tie!')
                    x = 0
            elif hit == 'quit':
                return False
               
                
    Shuffle()
    if Play() == False:
        return 0
    
x = 1  
while x != 0:
    x = Blackjack()
