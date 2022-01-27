import pandas as pd
import matplotlib.pyplot as plt
readCSV = pd.read_csv('FusionCorrigee.csv', index_col=False)
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
listeTV.sort()
listeSaison.sort()
plt.figure(figsize=(30,30))
plt.plot(listeSaison, listeTV )
plt.title('figure 1')
plt.xlabel('axe x')
plt.ylabel('axe y')
plt.savefig('fig.png')
plt.show()



