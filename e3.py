"""
24/01/2024
Ayman Dghoughi, Nizar El Khoulfi, Ian Díaz
ASIXcB e3 UF1
Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català i afegir la traducció en castellà, anglès i klingon
El programa, demanarà a l’usuari que escrigui per teclat un insult, en català, i el mostrarà traduït a castellà, anglès i klingon.
"""
exists = False
insults = {'CAT': ('CARALLOT', 'MOCÓS', 'MALPARIT', 'TROS DE QUÒNIAM', 'FLASCA', 'TARAL·LIROT', 'LLONDRO', 'ABRAÇAFANALS', 'AFAITAPAGESOS', 'BORDEGÀS'),
           'ESP': ('CARALLO', 'MOCOS', 'MALPARIDO', 'TROZO DE CARNE', 'FLEMA', 'TARAL·LIROT', 'TONTOLABA', 'ARRASTRADO', 'ADULADOR', 'APROVECHADO'),
           'ENG': ('JERK', 'SNOT', 'SCOUNDREL', 'BLOCKHEAD', 'PHLEGM', 'FOOL', 'DUNDERHEAD', 'GROVELER', 'SUCK-UP', 'EXPLOITER'),
           'KLI': ('KJERK', 'KSNOT', 'KSCOUNDREL', 'KBLOCKHEAD', 'KPHLEGM', 'KFOOL', 'KDUNDERHEAD', 'KGROVELER', 'KSUCK-UP', 'KEXPLOITER')}
insult = input().upper().replace(" ", "")
idiomes = ['CAT', 'ESP', 'ENG', 'KLI']
# Ejercicio no bonus:
for i in range(len(insults["CAT"])):
    if insults['CAT'][i] == insult:
        print(f'Espanyol:\t{insults["ESP"][i]}\nAnglès:\t\t{insults["ENG"][i]}\nKlingon:\t{insults["KLI"][i]}')

#Ejercicio bonus:
for x in idiomes:
    for i in range(len(insults[x])):
        if insults[x][i] == insult:
            print(f'idioma escollit: {x}, insult: {insults[x][i]}')
            idiomes.remove(x)
            for x in idiomes:
                print(f'{x}: {insults[x][i]}')
            exists = True
if exists == False:
    print("El insulto no existe en la lista.")