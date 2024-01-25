"""
24/01/2024
Ayman Dghoughi, Nizar El Khoulfi, Ian Díaz
ASIXcB e3 UF1
Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català i afegir la traducció en castellà, anglès i klingon
El programa, demanarà a l’usuari que escrigui per teclat un insult, en català, i el mostrarà traduït a castellà, anglès i klingon.
"""
exists = False
INSULTS = {'CAT': ('CARALLOT', 'MOCÓS', 'MALPARIT', 'TROS DE QUÒNIAM', 'FLASCA', 'TARAL·LIROT', 'LLONDRO', 'ABRAÇAFANALS', 'AFAITAPAGESOS', 'BORDEGÀS'),
           'ESP': ('CARALLO', 'MOCOS', 'MALPARIDO', 'TROZO DE CARNE', 'FLEMA', 'TARAL·LIROT', 'TONTOLABA', 'ARRASTRADO', 'ADULADOR', 'APROVECHADO'),
           'ENG': ('JERK', 'SNOT', 'SCOUNDREL', 'BLOCKHEAD', 'PHLEGM', 'FOOL', 'DUNDERHEAD', 'GROVELER', 'SUCK-UP', 'EXPLOITER'),
           'KLI': ('KJERK', 'KSNOT', 'KSCOUNDREL', 'KBLOCKHEAD', 'KPHLEGM', 'KFOOL', 'KDUNDERHEAD', 'KGROVELER', 'KSUCK-UP', 'KEXPLOITER')}
insult = input().upper().replace(" ", "")
idiomes = ['CAT', 'ESP', 'ENG', 'KLI']
# Ejercicio no bonus:
for i in range(len(INSULTS["CAT"])):
    if INSULTS['CAT'][i] == insult:
        print(f'Espanyol:\t{INSULTS["ESP"][i]}\nAnglès:\t\t{INSULTS["ENG"][i]}\nKlingon:\t{INSULTS["KLI"][i]}')

#Ejercicio bonus:
for x in idiomes:
    for i in range(len(INSULTS[x])):
        if INSULTS[x][i] == insult:
            print(f'idioma escollit: {x}, insult: {INSULTS[x][i]}')
            idiomes.remove(x)
            for x in idiomes:
                print(f'{x}: {INSULTS[x][i]}')
            exists = True
if exists == False:
    print("El insulto no existe en la lista.")