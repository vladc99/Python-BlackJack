import Game

playerName = input("Please enter your name:")
print("Hi " + playerName + " game has started, your initial balance is : $100")

restart = True
while restart:

    # Game is initialized
    game = Game.Game(playerName)

    playerBet = input("Please place your bet:")

    while not playerBet.isdecimal() or int(playerBet) < 0 or int(playerBet) > int(game.player.balance) \
            or int(playerBet) < 10:
        if not playerBet.isdecimal():
            print("Balance should be a positive number")
        else:
            if int(playerBet) > 0 or int(playerBet) > int(game.player.balance) or int(playerBet) < 10:
                print("Bet should be bigger than 10 and smaller then you balance!"
                      "\nYour Balance is: " + str(game.player.balance))

        playerBet = input("Please place your bet: ")

    # display the dealer card
    print("Dealer has the card:")
    game.dealer.showCard()

    # Check if player busted from beginning
    playerBust = game.checkPlayerBust()
    if playerBust:
        game.player.subBalance(playerBet) # Subtract Balance if player is busted
        game.player.showHand()
        answer = input(game.player.name + " busted! You lost " + playerBet + "\nPlay Again? Y or N? ")
        # Verify input
        while not answer.capitalize() == "N" or not answer.capitalize() == "Y":
            answer = input("Please input Y or N only")
        if answer.capitalize() == "N":
            exit()
    else:
        # Show player cards
        game.player.showHand()

        answer = input("1.Hit or 2.Stand?")
        # Verify input
        while not answer.isdecimal() or not int(answer) == 1 or not int(answer) == 2:
            answer = input("Please enter 1 or 2 ")

        # loop until the player want's to stop or if he's busted
        while int(answer) == 1:
            game.player.draw(game.deck.drawCard())
            game.player.showHand()
            playerBust = game.checkPlayerBust()
            if playerBust:
                print(playerName + " BUSTED")
                break
            answer = input("1.Hit or 2.Stand?")

        # When player stops and he's not busted it's dealer's turn
        if int(answer) == 2:
            dealerFinish = game.checkDealerBust()
            while not dealerFinish:
                if game.dealer.dealerShowScore() < 16:
                    game.dealer.dealerDraw(game.deck.drawCard())
                    dealerFinish = game.checkDealerBust()
                else:
                    print("Dealer turn finished")
                    game.dealer.dealerShowHand()
                    dealerFinish = True

        if ((int(game.player.showScore()) > int(game.dealer.dealerShowScore()))
            or int(game.dealer.dealerShowScore()) > 21) and (playerBust != True):

            game.player.addBalance(int(playerBet) * 2)
            playAgain = input("Player WON! " + str(int(playerBet) * 2) + "\nPlay Again? Y or N ")

            while not answer.capitalize() == "N" or not answer.capitalize() == "Y":
                answer = input("Please input Y or N only")
            if playAgain.capitalize() == "N":
                restart = False

            print("Your new balance is: " + game.player.balance)
        else:
            playAgain = input("Dealer WON! You lost " + playerBet + "\nPlay Again? Y or N ")
            game.player.subBalance(playerBet)
            print("Your new balance is: " + str(game.player.balance))
            if playAgain.capitalize() == "N":
                restart = False
