import random

percorso = ['_' for i in range(70)]

posTartaruga = 1
posLepre = 1
energiaTartaruga = 100
energiaLepre = 100
meteo = "soleggiato"


def mossaTartaruga():
    global posTartaruga

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
    

def mossaLepre():
    global posLepre

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

    
    

def stampaPercorso(start = 0):
    global percorso
    [print(percorso[i]) for i in range(start, 70)]


def mainLoop():
    global posTartaruga
    global posLepre

    tick = 1
    flagFineGara = False

    posTartaruga = 1
    posLepre = 1
    print("Start the Race!")

    while not flagFineGara:
        print("\nTick: ", tick)
        
        mossaTartaruga()
        mossaLepre()

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


ostacoli = {15: -3, 30: -5, 45: -7}
bonus = {10: 5, 25: 3, 50: 10}



def mossaTartarugaExtra():
    global posTartaruga
    global energiaTartaruga
    global meteo
    global ostacoli
    global bonus
    global percorso

    estrazione = random.randint(1,10)
    posTartarugaPrecedente = posTartaruga
    
    if estrazione <= 5:         # Passo Veloce 50% +3 en-5
        if energiaTartaruga >= 5:
            energiaTartaruga -= 5
            posTartaruga += 3
        else:
            energiaTartaruga += 10
    
    elif estrazione <= 7:       # Scivolata 20% -6 en-10
        if energiaTartaruga >= 10:
            energiaTartaruga -= 10
            posTartaruga -= 6
        else:
            energiaTartaruga += 10
    
    else:                       # Passo Lento 30% +1 en-3
        if energiaTartaruga >= 3:
            energiaTartaruga -= 3
            posTartaruga += 1
        else:
            energiaTartaruga += 10


    if energiaTartaruga > 100:
        energiaTartaruga = 100

    if meteo == 'pioggia':
        posTartaruga -= 1

    if posTartaruga < 1:
        posTartaruga = 1

    if posTartaruga in ostacoli:
        posTartaruga += ostacoli[posTartaruga]
    if posTartaruga in bonus:
        posTartaruga += bonus[posTartaruga]

    if posTartaruga < 1:
        posTartaruga = 1

    if posTartaruga > 70:
        posTartaruga = 70

    percorso[posTartarugaPrecedente - 1] = '_'
    percorso[posTartaruga - 1] = 'T'

    

def mossaLepreExtra():
    global posLepre
    global energiaLepre
    global meteo
    global ostacoli
    global bonus
    global percorso

    estrazione = random.randint(1,10)
    posLeprePrecedente = posLepre

    if estrazione <= 2:         # Riposo 20% +0 en+10
        energiaLepre += 10
        posLepre += 0
    
    elif estrazione <= 4:       # Grande Balzo 20% +9 en-15
        if energiaLepre >= 15:
            energiaLepre -= 10    
            posLepre += 9
        else:
            energiaLepre += 10

    elif estrazione <= 5:       # Grande Scivolata 10% -12 en-20
        if energiaLepre >= 20:
            energiaLepre -= 20
            posLepre -= 12
        else:
            energiaLepre += 10
    
    elif estrazione <= 8:       # Piccolo Balzo 30% +1 en-5
        if energiaLepre >= 5:
            energiaLepre -= 5
            posLepre += 1
        else:
            energiaLepre += 10

    else:                       # Piccola Scivolata 20% en-8
        if energiaLepre >= 8:
            energiaLepre -= 8
            posLepre -= 2
        else:
            energiaLepre += 10

    
    if energiaLepre > 100:
        energiaLepre = 100
    
    if meteo == 'pioggia':
        posLepre -= 2
    
    if posLepre < 1:
        posLepre = 1

    if posLepre in ostacoli:
        posLepre += ostacoli[posLepre]
    if posLepre in bonus:
        posLepre += bonus[posLepre]

    if posLepre < 1:
        posLepre = 1

    if posLepre > 70:
        posLepre = 70

    percorso[posLeprePrecedente - 1] = '_'
    percorso[posLepre - 1] = 'L'


def mainLoopExtra():
    global meteo
    global posLepre
    global posTartaruga
    global percorso

    tick = 1
    tickFlag = True
    flagFineGara = False

    posTartaruga = 1
    posLepre = 1
    print("Start the Race!")

    while not flagFineGara:
        print("\nTick: ", tick)
        
        mossaTartarugaExtra()
        mossaLepreExtra()

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

        if tick % 10 == 0:
            tickFlag = not tickFlag
            if tickFlag:
                meteo = "pioggia"
            else:
                meteo = "soleggiato"
    

mainLoop()
print("####################################################################")
percorso = ['_' for i in range(70)]
mainLoopExtra()