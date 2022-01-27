import pandas as pd

counter = 0
movieCounter = 0
frenchMovies = 0

readCSV = pd.read_csv('../../output/finalMerge.csv', index_col=False)

while True:
    try:
        cellCheck = pd.isnull(readCSV.iloc[counter, 1])
    except IndexError:
        break
    if cellCheck == False:
        movie = readCSV.iloc[counter, 1]
        if movie == "Movie":
            cellCheck = pd.isnull(readCSV.iloc[counter, 5])
            movieCounter += 1
            if cellCheck == False:
                movie = readCSV.iloc[counter, 5]
                movieSearch = movie.find("France")
                if movieSearch != -1:
                    frenchMovies += 1
    counter += 1

print(f"Il y a {frenchMovies} films sur {movieCounter} films qui ont été produits en France")
