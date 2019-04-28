from class_card import Card
from class_player import Player
from class_deck import Deck
class Game:
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def print_winner(self, winner):
        w = "{} wins this round"
        w = w.format(winner.name)
        print(w)

    def print_draw(self, p1, p2):
        d = "{} drew {} {} drew {}"
        d = d.format(p1.name, p1.card, p2.name, p2.card)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any key to play:"
            response = input(m)
            if response == 'q':
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2)

        win = self.winner(self.p1, self.p2)
        print("War is over.{} wins".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"