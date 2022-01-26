import pandas as pd
import os


def merge():
    for i in range(1, 6):
        read = pd.read_csv(f"../../../data/raw/netflix-{i}.csv", header=None)
        read = read.drop(read.columns[11], axis=1)
        read.to_csv(f"output{i}.csv", index=False)

    df = pd.concat(
        map(pd.read_csv, ['output1.csv', 'output2.csv', 'output3.csv', 'output4.csv', 'output5.csv']),
        ignore_index=True)

    df.to_csv("fusion.csv", index=False)

    for i in range(1, 6):
        os.remove(f"output{i}.csv")


def getNumberOfRowsAndColummns():
    pass


def valueCheck(file, nbLines):
    read = pd.read_csv(file, index_col=False)
    missingValue = 0
    aberrantValue = 0
    missingValueColumn = 0
    delList = []

    for i in range(1, nbLines):
        try:
            added = read.iloc[i, 6]
            released = int(read.iloc[i, 7])
            nothing, added = added.split(",")
            added = int(added)
        except:
            delList.append(i)
            missingValue += 1
            missingValueColumn += 1
        if added < released:
            aberrantValue += 1
            print(added, released, f"--> Valeur Abérante Ligne s{i}")
            delList.append(i)
        for n in range(0, 11):
            cellCheck = pd.isnull(read.iloc[i, n])
            if cellCheck == True:
                missingValue += 1

    read.drop(read.index[delList], inplace=True)
    read.to_csv('FusionCorrigee.csv', index=False)

    return aberrantValue, missingValue, missingValueColumn,


def crossProduct(x):
    calc = x * 100 / 8808
    return calc


def frenchMovies(file):
    readCSV = pd.read_csv(file, index_col=False)
    counter = 0
    movieCounter = 0
    frenchMovies = 0

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
    return frenchMovies, movieCounter


def displayResults():
    pass
