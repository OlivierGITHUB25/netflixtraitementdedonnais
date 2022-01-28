import pandas as pd
import matplotlib.pyplot as plt
import re
import csv

#readCSV = pd.read_csv('../../output/finalMerge.csv', index_col=False)
with open('../../output/finalMerge.csv','r') as file:
    reader = list(csv.reader(file))
    for i in range(len(reader)):
        print(reader[i])

counter = 0
ligne=0
listeTV=[]
listeSaison=[]
listeSaisonM=[]
total = 0
conteur=0
dateListe = []
'''
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
                for i in range(1900, 2050):
                    series = readCSV.iloc[ligne, 7]
                    if series == str(i):
                        ligne+=1
                        conteur += 1
                        TV = readCSV.iloc[counter, 9]
                        total += int(re.findall('\d+', f'{TV}')[0] )


        counter += 1
total=total/conteur
listeSaison.append(total)
print(f"{listeSaison},{total},{conteur}")'''