import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()
        self.shuffle()

    def build(self):
        for s in ["Spades", "Diamonds", "Clubs", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card.Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

    def getHand(self):
        return self.hand
