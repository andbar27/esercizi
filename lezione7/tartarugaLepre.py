import random

percorso = ['_' for i in range(70)]


def mossaTartaruga(posTartaruga):
    estrazione = random.randint(1,10)
    posTartarugaPrecedente = posTartaruga

    if estrazione <= 5:         # Passo Veloce 50% +3
        posTartaruga += 3
    
    elif estrazione <= 7:       # Scivolata 20% -6
        posTartaruga -= 6
        if posTartaruga < 1:
            posTartaruga = 1
    
    else:                       # Passo Lento 30% +1
        posTartaruga += 1


    if posTartaruga > 70:
        posTartaruga = 70

    percorso[posTartarugaPrecedente - 1] = '_'
    percorso[posTartaruga - 1] = 'T'

    return posTartaruga
    

def mossaLepre(posLepre):
    estrazione = random.randint(1,10)
    posLeprePrecedente = posLepre

    if estrazione <= 2:         # Riposo 20% +0
        posLepre += 0
    
    elif estrazione <= 4:       # Grande Balzo 20% +9
        posLepre += 9

    elif estrazione <= 5:       # Grande Scivolata 10% -12
        posLepre -= 12
        if posLepre < 1:
            posLepre = 1
    
    elif estrazione <= 8:       # Piccolo Balzo 30% +1
        posLepre += 1

    else:                       # Piccola Scivolata
        posLepre -= 2
        if posLepre < 1:
            posLepre = 1


    if posLepre > 70:
        posLepre = 70

    percorso[posLeprePrecedente - 1] = '_'
    percorso[posLepre - 1] = 'L'

    return posLepre

    
    

def stampaPercorso(start = 0):
    [print(percorso[i]) for i in range(start, 70)]


def mainLoop():
    tick = 1
    flagFineGara = False

    posTartaruga = 1
    posLepre = 1
    print("Start the Race!")

    while not flagFineGara:
        print("\nTick: ", tick)
        
        posTartaruga = mossaTartaruga(posTartaruga)
        posLepre = mossaLepre(posLepre)

        if posLepre == posTartaruga:
            percorso[posLepre - 1] = 'OUCH!!!'
            stampaPercorso(posLepre - 1)
        else:
            stampaPercorso()
        

        traguardo = percorso[70 - 1]
        
        if traguardo == 'T':
            print("TORTOISE WINS! || VAY!!!")
            flagFineGara = True
        
        elif traguardo == 'L':
            print("HARE WINS || YUCH!!!")
            flagFineGara = True
        
        elif traguardo == 'OUCH!!!':
            print("IT'S A TIE.")
            flagFineGara = True

        
        tick += 1



mainLoop()