import Player


def dealerStand():
    print("Dealer Stands")


class Dealer:
    def __init__(self, card1, card2):
        self.dealer = Player.Player("Dealer", card1, card2)

    def showCard(self):
        print(self.dealer.returnFirstCard().show())

    def dealerShowScore(self):
        score = 0
        for card in self.dealer.hand:
            score += card.getScore()
        return score

    def dealerShowHand(self):
        self.dealer.showHand()

    def dealerDraw(self, card):
        self.dealer.draw(card)