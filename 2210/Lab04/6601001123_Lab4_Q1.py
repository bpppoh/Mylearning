def printDeck(deck) :
    string = ''
    for i in range(len(deck)) :
        string += ' ' + deck[i]
    print(string)

try :
    deck = input("Please enter the cards in the deck (seperates by spaces): ").split()
    command = input("Please enter the commands (e.g. CSCS): ")
    for i in range(len(command)) :
        match command[i].lower() :
            case 'c' :
                mid = len(deck) // 2
                deck = deck[mid:] + deck[:mid]
                printDeck(deck)
            case 's' :
                tempDeck = []
                for i in range(len(deck)//2) :
                    tempDeck.append(deck[i])
                    tempDeck.append(deck[ (len(deck)//2) + i])
                deck = tempDeck
                printDeck(deck)
except:
    print("Error")