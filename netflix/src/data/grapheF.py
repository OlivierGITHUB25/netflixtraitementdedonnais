import pandas as pd
import matplotlib.pyplot as plt
import re

readCSV = pd.read_csv('../../output/finalMerge.csv', index_col=False)
TVCounter = 0
counter = 0
listeTV=[]
listeSaison=[]
listeSaisonM=[]
total = 0
conteur=0
for i in range(1900, 2050):
    while True:
        try:
            cellCheck = pd.isnull(readCSV.iloc[counter, 1])
        except IndexError:
            break
        if cellCheck == False:
            series = readCSV.iloc[counter, 1]
            print("test0")
            if series == "TV Show":
                cellCheck = pd.isnull(readCSV.iloc[counter, 7])
                TVCounter += 1
                print("test1")
                if cellCheck == False:
                    series = readCSV.iloc[counter, 7]
                    print("test2")
                    i = str(f"{i}")
                    if series == "2020":
                        conteur += 1
                        print("test3")
                        TV = readCSV.iloc[counter, 9]
                        number, bin = TV.split(" ")
                        total+=int(re.findall('\d+', f'{number}')[0] )


        counter += 1
total=total/conteur
listeSaison.append(total)
print(f"{listeSaison},{total},{conteur}")