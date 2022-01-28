import pandas as pd
import matplotlib.pyplot as plt
import re

readCSV = pd.read_csv('../../output/finalMerge.csv', index_col=False)
counter = 0
listeTV=[]
listeSaison=[]
listeSaisonM=[]
total = 0
conteur=0
dateListe = []

while True:
    try:
        CellCheck = pd.isnull(readCSV.iloc[counter, 1])
    except IndexError:
        break
    if CellCheck == False:
        series = readCSV.iloc[counter, 1]
        if series == "TV Show":
            CellCheck = pd.isnull(readCSV.iloc[counter, 7])
            if CellCheck == False:
                for i in range(1900, 2051):
                    series = readCSV.iloc[counter, 7]
                    if series == str(i):
                        conteur += 1
                        TV = readCSV.iloc[counter, 9]
                        total += int(re.findall('\d+', f'{TV}')[0] )


        counter += 1
total=total/conteur
listeSaison.append(total)
print(f"{listeSaison},{total},{conteur}")