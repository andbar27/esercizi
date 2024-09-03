import os

def CercaStringaInFileName(sFile, sString):
    if sString.lower() in sFile.lower():
        return True
    return False


def CercaStringaInFile(sFile, sString):
    try:
        with open(sFile, "r") as f:
            lines = f.readlines()
            for line in lines:
                if sString in line:
                    return True
    except Exception:
        print("impossibile leggere file: ", sFile)
    return False
# i
#IMMISSIONE DEI PARAMETRI
sRoot = input("Inserisci la root directory: ")
sStringaDaCercare = input("Inserisci la stringa da cercare: ")
sOutDir = input("Inserisci la dir di output: ")

#NAVIGA NEL FILE SYSTEM
fileRet = []
iNumFileTrovati = 0
for root, dirs, files in os.walk(sRoot):
    # .format() - non serve utilizzare la f davanti, e puoi riferirti tramite numeri al valore
    sToPrint = "Dir corrente {0} contenente {1} subdir e {2} files".format(root, len(dirs), len(files))
    print(sToPrint)

    
    for filename in files:
        #iRet = CercaStringaInFileName(filename,sStringaDaCercare)
        iRet = CercaStringaInFile(root+'/'+filename,sStringaDaCercare)
        if(iRet == True):
            print("Trovato file: ",filename)
            fileRet.append(root+'/'+filename)
            iNumFileTrovati = iNumFileTrovati + 1

print("\n\n",fileRet, "numero file: ", iNumFileTrovati,"\n\n")

os.mkdir(sRoot + sOutDir)

import shutil
for nameFile in fileRet:
    shutil.copy(nameFile, sRoot + sOutDir)