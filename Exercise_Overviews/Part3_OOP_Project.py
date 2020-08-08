#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.cards = []
        for s in SUITE:
            for r in RANKS:
                self.cards.append((s, r))
        print(self.cards)

    def shuffle_cards(self):
        shuffle(self.cards)

    def split_cards(self):
        p1_cards = self.cards[:26]
        p2_cards = self.cards[26:]
        return p1_cards, p2_cards


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards):
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self):
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.hand = hand
        self.name = name

    def check_cards(self):
        if len(self.hand.cards) == 0:
            return False
        return True


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

deck = Deck()
deck.shuffle_cards()

p1_cards, p2_cards = deck.split_cards()

p1_hand = Hand(p1_cards)
p2_hand = Hand(p2_cards)

player1 = Player("player1", p1_hand)
player2 = Player("player2", p2_hand)

while (True):
    if not player1.check_cards():
        break
    if not player2.check_cards():
        break

    p1_card = player1.hand.remove_card()
    p2_card = player2.hand.remove_card()

    print("p1_card : {}".format(p1_card))
    print("p2_card : {}".format(p2_card))

    p1_rank = RANKS.index(p1_card[1])
    p2_rank = RANKS.index(p2_card[1])

    if p1_rank > p2_rank:
        print("Player 1 won the deal")
        player1.hand.add_card(p2_card)
        player1.hand.add_card(p1_card)
        print(player1.hand.cards)
    elif p2_rank > p1_rank:
        print("Player 2 won the deal")
        player2.hand.add_card(p1_card)
        player2.hand.add_card(p2_card)
        print(player2.hand.cards)
    else:
        print("**********DRAW**********")
        p1 = []
        p2 = []
        for i in range(0, 3):
            if player1.check_cards() and player2.check_cards():
                p1.append(player1.hand.remove_card())
                p2.append(player2.hand.remove_card())
            else:
                break

        sum1 = sum2 = 0
        for i in range(0, len(p1)):
            sum1 += RANKS.index(p1[i][1])
            sum2 += RANKS.index(p2[i][1])

        if sum1 > sum2:
            print("Player 1 won the deal")
            for i in p2:
                player1.hand.add_card(i)
            for i in p1:
                player1.hand.add_card(i)
            print(player1.hand.cards)
        elif sum2 > sum1:
            print("Player 2 won the deal")
            for i in p1:
                player2.hand.add_card(i)
            for i in p2:
                player2.hand.add_card(i)
            print(player2.hand.cards)
        else:
            print("----------------AGAIN DRAW----------------")
            if player1.check_cards() and player2.check_cards():
                newcard1 = player1.hand.remove_card()
                newcard2 = player2.hand.remove_card()
            else:
                break

            rank1 = RANKS.index(newcard1[1])
            rank2 = RANKS.index(newcard2[1])

            if rank1 > rank2:
                print("Player 1 won the deal")
                for i in p2:
                    player1.hand.add_card(i)
                player1.hand.add_card(newcard1)
                print(player1.hand.cards)
            else:
                print("Player 2 won the deal")
                for i in p1:
                    player2.hand.add_card(i)
                player2.hand.add_card(newcard1)
                print(player2.hand.cards)

if player1.check_cards():
    print("==========************Player 1 is the winner***********==========")
    print(player1.hand.cards)
else:
    print("==========************Player 2 is the winner***********==========")
    print(player2.hand.cards)


# Use the 3 classes along with some logic to play a game of war!
