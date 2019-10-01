def stand():
    return False


class Player:
    def __init__(self, name, card1, card2):
        self.name = name
        self.hand = [card1, card2]
        self.balance = 100
        self.score = self.showScore()

    def draw(self, card):
        self.hand.append(card)
        return self

    def showHand(self):
        print("Cards in hand for "+self.name)
        for card in self.hand:
            card.show()
        print("Score: "+str(self.showScore()))

    def showScore(self):
        score = 0
        for card in self.hand:
            score += card.getScore()
        return score

    def returnFirstCard(self):
        return self.hand[0]

    def addBalance(self, val):
        self.balance += int(val)

    def subBalance(self, val):
        self.balance -= int(val)

    def viewBalance(self):
        print(self.balance)
