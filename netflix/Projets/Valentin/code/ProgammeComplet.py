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

    df.to_csv("Merge.csv", index=False)

    for i in range(1, 6):
        os.remove(f"output{i}.csv")


def getNumberOfRows(file):
    read = pd.read_csv(file, index_col=False)
    counter = 0
    while True:
        counter += 1
        try:
            read.iloc[counter, 0]
        except IndexError:
            break
        except:
            continue
    return counter


def valueCheck(file, nbLines):
    read = pd.read_csv(file, index_col=False)
    missingValue = 0
    aberrantValue = 0
    missingValueColumn = 0
    delList = []

    for counter in range(1, nbLines):
        try:
            added = read.iloc[counter, 6]
            released = int(read.iloc[counter, 7])
            nothing, added = added.split(",")
            added = int(added)
        except:
            delList.append(counter)
            missingValue += 1
            missingValueColumn += 1
        if released > added:
            aberrantValue += 1
            print(added, released, f"--> Valeur Abérante Ligne s{counter}")
            delList.append(counter)
        for n in range(0, 11):
            cellCheck = pd.isnull(read.iloc[counter, n])
            if cellCheck == True:
                missingValue += 1

    read.drop(read.index[delList], inplace=True)
    read.to_csv('FinalMerge.csv', index=False)

    return aberrantValue, missingValue, missingValueColumn


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

try:
    merge()
except PermissionError:
    print("Le fichier n'est pas accessible car il est ouvert")
except:
    print("La fusion a échouée")
else:
    mergeFile = "Merge.csv"
    finalMergeFile = "FinalMerge.csv"
    numberOfRows = getNumberOfRows(mergeFile)
    aberrantValue, missingValue, missingValueColumn = valueCheck(mergeFile, numberOfRows)
    numberOfRows = getNumberOfRows(finalMergeFile)
    calc = lambda x : x * 100 / numberOfRows
    total = aberrantValue + missingValueColumn
    frenchMovies, movieCounter = frenchMovies(finalMergeFile)
    os.remove("Merge.csv")
    print(f"--------------------------------\n"
          f"NOMBRE VALEURS MANQUANTES TOTALES : {missingValue}\n"
          f"Pourcentage : {calc(missingValue):.2f}\n"
          f"--------------------------------\n"
          f"NOMBRE VALEURS MANQUANTES (Col 6 et 7): {missingValueColumn}\n"
          f"Pourcentage : {calc(missingValueColumn):.2f}\n"
          f"--------------------------------\n"
          f"NOMBRE VALEURS ABERANTES (Col 6 et 7): {aberrantValue}\n"
          f"Pourcentage : {calc(aberrantValue):.2f}\n"
          f"--------------------------------\n"
          f"Total d'erreur (Col 6 et 7): {total}\n"
          f"Pourcentage d'erreur total : {calc(total):.2f}\n"
          f"--------------------------------\n"
          f"SEUL LES COLONNES 6 ET 7 ONT ÉTÉ CORRIGÉ DANS LE FICHIER FINAL\n"
          f"--------------------------------\n"
          f"{frenchMovies}/{movieCounter} films ont été produits en France\n")

