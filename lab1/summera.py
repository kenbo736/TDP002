######### up1 a ################################################################
summa = 0

for i in range(1, 513):
    summa = i + summa

#print(summa)
################################################################################

######### up1 b ################################################################
produkt = 1

for x in range(1, 513):
    produkt = x * produkt

#print(produkt)
################################################################################

######### up1 c ################################################################
heltal = 0
run = True

while run:
    heltal = heltal + 1
    for dela in range(1, 14):
        if(heltal%dela) > 0:
            break
        elif(dela == 14-1):
            #print(heltal)
            run = False

#print(heltal)
################################################################################

######### up1 d ################################################################
primSum = 0

for number in range(2, 1001):
    for checkIfPrim in range(2, number):
        if(number%checkIfPrim) == 0:
            break
        elif checkIfPrim == (number-1):
            #print(number)
            primSum = number + primSum

#behöver lägga till 2 i slutet för att 2 är ett undantag som ett primtal
print(primSum+2)
