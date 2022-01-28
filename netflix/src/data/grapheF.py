import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import re
#import csv

#readCSV = pd.read_csv('../../output/finalMerge.csv', index_col=False)
#with open('../../output/finalMerge.csv','r') as file:
    #reader = list(csv.reader(file))
    #for i in range(len(reader)):
        #print(reader[i])

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

#listeTV.sort()
#listeSaison.sort()
#plt.figure(figsize=(30,30))
#plt.plot(listeSaison, listeTV )
#plt.title('figure 1')
#plt.xlabel('axe x')
#plt.ylabel('axe y')
#plt.savefig('fig.png')
#plt.show()

readCSV = pd.read_csv('../../output/finalMerge.csv', index_col=False)
TVCounter = 0
counter = 0
listeTV=[]
listeSaison=[]

while True:
    try:
        cellCheck = pd.isnull(readCSV.iloc[counter, 1])
    except IndexError:
        break
    if cellCheck == False:
        series = readCSV.iloc[counter, 1]
        if series == "TV Show":
            cellCheck = pd.isnull(readCSV.iloc[counter, 7])
            TVCounter += 1
            if cellCheck == False:
                TV = readCSV.iloc[counter, 7]
                listeTV.append(TV)

    counter += 1

print(f"Voici la liste des annès des series {listeTV}")

counter = 0
cellCheck = 0
series = 0
tv =0

while True:
    try:
        cellCheck = pd.isnull(readCSV.iloc[counter, 1])
    except IndexError:
        break
    if cellCheck == False:
        series = readCSV.iloc[counter, 1]
        if series == "TV Show":
            cellCheck = pd.isnull(readCSV.iloc[counter, 9])
            TVCounter += 1
            if cellCheck == False:
                TV = readCSV.iloc[counter, 9]
                number, bin = TV.split(" ")
                listeSaison.append(number)

    counter += 1
print(f"Voici la liste des annès des series {listeSaison}")
dict = {'sasison': listeSaison, 'TV': listeTV,}
df = pd.DataFrame(dict)
df.to_csv('test.csv')


readCSV2 = pd.read_csv('test.csv')
print("test0")
for i in range(1900, 2050):
    print("test1.5")
    while True:
        try:
            print("test1")
            cellCheck = pd.isnull(readCSV2.iloc[counter, 2])
        except IndexError:
            break
        if cellCheck == False:
            series = readCSV2.iloc[counter, 2]
            print("test2")
            if series == str(i):
                print("test3")
                conteur += 1
                TV = readCSV2.iloc[counter, 2]
                total += int(re.findall('\d+', f'{TV}')[0])
        counter += 1

total=total/conteur
listeSaison.append(total)
print(f"{listeSaison},{total},{conteur}")