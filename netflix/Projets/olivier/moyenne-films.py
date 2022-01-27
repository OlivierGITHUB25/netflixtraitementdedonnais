import pandas as pd
import statistics
readCSV = pd.read_csv('FusionCorrigee.csv', index_col=False)
moyenneF=0
total=0
movieCounter = 0
counter = 0
liste=[]
med =0

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
                total+= movie
                liste.append(movie)

    counter += 1
moyenneF=total/movieCounter
med=statistics.median(liste)

print(f"Il y a {movieCounter} pour une durée de  {total} min nous avons donc une moyenne  de {moyenneF:.2f} min par film et une mediane de {med}")