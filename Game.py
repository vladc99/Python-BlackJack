import Deck
import Player
import Dealer


class Game:
    def __init__(self, playerName):
        self.deck = Deck.Deck()
        self.player = Player.Player(playerName, self.deck.drawCard(), self.deck.drawCard())
        self.dealer = Dealer.Dealer(self.deck.drawCard(), self.deck.drawCard())

    def checkPlayerBust(self):
        if int(self.player.showScore()) > 21:
            return True
        else:
            return False

    def checkDealerBust(self):
        if int(self.dealer.dealerShowScore()) > 21:
            print("Dealer Busted")
            return True
        else:
            return False
