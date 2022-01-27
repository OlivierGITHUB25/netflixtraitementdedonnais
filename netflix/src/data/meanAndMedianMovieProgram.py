import pandas as pd
import statistics

moyenneF=0
total=0
movieCounter = 0
counter = 0
liste=[]
med =0

readCSV = pd.read_csv('../../output/finalMerge.csv', index_col=False)

while True:
    try:
        cellCheck = pd.isnull(readCSV.iloc[counter, 1])
    except IndexError:
        break
    if cellCheck == False:
        movie = readCSV.iloc[counter, 1]
        if movie == "Movie":
            cellCheck = pd.isnull(readCSV.iloc[counter, 9])
            movieCounter += 1
            if cellCheck == False:
                movie = readCSV.iloc[counter, 9]
                movie = int(movie[:-3])
                total += movie
                liste.append(movie)

    counter += 1

mean = total/movieCounter
median = statistics.median(liste)

print(f"Il y a {movieCounter} pour une durée de  {total} min nous avons donc une moyenne  de {mean:.2f} min par film et une mediane de {median}")