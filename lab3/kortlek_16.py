from random import shuffle
import copy

abcList = [0]
for abc in range(65, 91):
    abcList.append(chr(abc))

def create_card(color, value):
    card = (color, value)
    return card

def get_value(card):
    #print(card[1])
    return card[1]

def get_suite(card):
    print(card[0])
    return card[0]

def suite_name(x):
    return{
    1: 'hearts',
    2: 'spades',
    3: 'diamonds',
    4: 'clovers',
    }[x]

def display_card(card):
    print(get_value(card), "of", suite_name(get_suite(card)))

def create_deck():
    deck = ["Deck", [("Joker A"), ("Joker B")]]
    for color in range(1, 5):
        for value in range(1, 14):
            card = create_card(color, value)
            deck[1].append(card)
    shuffle(deck[1])
    return deck

def pick_card(bunchOfCards):
    topCard = bunchOfCards[1][0]
    return topCard

def insert_card(pickCard, bunchOfCards):
    #insert card at the top of the deck
    cardRemove = bunchOfCards[1].remove(pickCard)
    cardInsert = bunchOfCards[1].append(pickCard)

def solitaire_keystream(length, bunchOfCards):
    #1
    #shuffle(bunchOfCards)
    keyPhrase = []

    #2
    while len(keyPhrase) < length:
        if "Joker A" == bunchOfCards[1][53]:
            bunchOfCards[1].remove("Joker A")
            bunchOfCards[1].insert(1, "Joker A")
            #print(bunchOfCards)
        else:
            JokerPos = bunchOfCards[1].index("Joker A")
            bunchOfCards[1].remove("Joker A")
            bunchOfCards[1].insert(JokerPos+1, "Joker A")
            #print(bunchOfCards)

        #3
        if "Joker B" == bunchOfCards[1][53]:
            bunchOfCards[1].remove("Joker B")
            bunchOfCards[1].insert(2, "Joker B")
            #print(bunchOfCards)
        elif "Joker B" == bunchOfCards[1][52]:
            bunchOfCards[1].remove("Joker B")
            bunchOfCards[1].insert(1, "Joker B")
        else:
            JokerPos = bunchOfCards[1].index("Joker B")
            bunchOfCards[1].remove("Joker B")
            bunchOfCards[1].insert(JokerPos+2, "Joker B")
            #print(bunchOfCards)

            #4
        jokerPosiA = bunchOfCards[1].index("Joker A")
        jokerPosiB = bunchOfCards[1].index("Joker B")
        #print(jokerPosiA, jokerPosiB)
        partA = []
        partB = []
        partC = []
        listCBA = []
        #separate cards into three groups
        if jokerPosiA < jokerPosiB:
            for a in range(0, jokerPosiA):
                partA.append(bunchOfCards[1][a])
            #print("Group A: ", partA, "\n")
            for b in range(jokerPosiA+1, jokerPosiB):
                partB.append(bunchOfCards[1][b])
            #print("Group B: ", partB, "\n")
            for c in range(jokerPosiB+1, 53):
                partC.append(bunchOfCards[1][c])
            #print("Group C: ", partC, "\n")

        elif jokerPosiA > jokerPosiB:
            for a in range(0, jokerPosiB):
                partA.append(bunchOfCards[1][a])
            #print("Group A: ", partA, "\n")
            for b in range(jokerPosiB+1, jokerPosiA):
                partB.append(bunchOfCards[1][b])
            #print("Group B: ", partB, "\n")
            for c in range(jokerPosiA+1, 53):
                partC.append(bunchOfCards[1][c])
            #print("Group C: ", partC, "\n")

        for c in range(0, len(partC)):
            listCBA.append(partC[c])
        for b in range(0, len(partB)):
            listCBA.append(partB[b])
        for a in range(0, len(partA)):
            listCBA.append(partA[a])
        #print(listCBA, "\n")

        #5
        #print("Last Card: ", listCBA[50])
        lastCardlist = listCBA[50]
        valueOfLastCard = get_value(lastCardlist)
        lastCardIndex = listCBA.index(listCBA[49])
        for rm in range(0, valueOfLastCard):
            card = listCBA[rm]
            listCBA.pop(rm)
            listCBA.insert(lastCardIndex, card)
        #print(listCBA, "\n")

        #6
        print("First Card: ", listCBA[0])
        firstCardlist = listCBA[0]
        valueOfFirsCard = get_value(firstCardlist)
        #print("DAAAAAAAAAAAAAAAAAAAAAA", valueOfFirstCard)
        keyCard = listCBA[valueOfFirsCard+1]
        keyCardlist = list(keyCard)
        valueOfKeyCard = keyCardlist[1]

        #print(abcList)
        abcKey = abcList[valueOfKeyCard]
        #keyPhrase = []
        keyPhrase.append(abcKey)
        keyPhraseString = ''.join(keyPhrase)
        #print(keyPhraseString)
    return keyPhraseString

def solitaire_encrypt(phrase, bunchOfCards):
    print(bunchOfCards)
    phrase = phrase.upper()
    test = solitaire_keystream(length, bunchOfCards)
    print("Nyckelfras: ", test)
    listResult = []
    for toI in range(0, len(phrase)):
        val = abcList.index(test[toI]) + abcList.index(phrase[toI])
        if(val <= 26):
            listResult.append(abcList[val])
        else:
            listResult.append(abcList[val-26])

    listResultString = ''.join(listResult)
    print("Encrypt: ", listResultString)
    return listResultString

def solitaire_decrypt(secret_message, bunchOfCards2):
    #1
    print(bunchOfCards2)
    secret_message_list = list(secret_message)
    secret_message_list_int = []
    listResult = []
    test = solitaire_keystream(length, bunchOfCards2)
    print("Nyckelfras2: ", test)
    for abc in range(0, len(secret_message_list)):
        number = ord(secret_message_list[abc])
        abc_number = number-64
        secret_message_list_int.append(abc_number)
    print(secret_message_list_int)

    #2
    fras_list = list(test)
    fras_list_int = []

    #3
    for abcd in range(0, len(fras_list)):
        number = ord(fras_list[abcd])
        abc_number = number-64
        fras_list_int.append(abc_number)
    print(fras_list_int)

    #4
    for toS in range(0, len(secret_message)):
        val = abcList.index(secret_message_list[toS]) - abcList.index(fras_list[toS])
        if(val < 1):
            listResult.append(abcList[val+26])
        else:
            listResult.append(abcList[val])
    listResultString = ''.join(listResult)
    print(listResultString)
    return listResultString

############### The use of the functions ################################

bunchOfCards = create_deck() #returns every card
bunchOfCards2 = copy.deepcopy(bunchOfCards)


#print(bunchOfCards2)
#kopia av bunchofcards
#pickCard = pick_card(bunchOfCards) #prints the top card of the deck
card = create_card(3, 2) #a card
#get_value(card)
#get_suite(card)
display_card(card)
#inserCard = insert_card(pickCard, bunchOfCards)
kryptMessage = "Python"
length = len(kryptMessage)
#solitaire_keystream(length, bunchOfCards)
#print(bunchOfCards)
secret_message = solitaire_encrypt(kryptMessage, bunchOfCards)
#print(secret_message)
#print(bunchOfCards2)
solitaire_decrypt(secret_message, bunchOfCards2)
#print(bunchOfCards)
