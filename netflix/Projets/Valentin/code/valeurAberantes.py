import pandas as pd

read = pd.read_csv('fusion.csv', index_col=False)
vaManquante = 0
vaAberante = 0
vaManquanteCol = 0
delList = []
counter = 0

while True:
    counter += 1
    try:
        added = read.iloc[counter, 6]
        released = int(read.iloc[counter, 7])
        nothing, added = added.split(",")
        added = int(added)
    except IndexError:
        break
    except:
        delList.append(counter)
        vaManquante += 1
        vaManquanteCol += 1
    if added < released:
        vaAberante += 1
        print(added, released, f"--> Valeur Abérante Ligne s{counter}")
        delList.append(counter)
    for n in range(0, 11):
        cellCheck = pd.isnull(read.iloc[counter, n])
        if cellCheck == True:
            vaManquante += 1

calc = lambda x : x * 100 / counter
read.drop(read.index[delList], inplace=True)
read.to_csv('FusionCorrigee.csv', index=False)
total = vaAberante + vaManquanteCol

print(f"--------------------------------\n"
      f"NOMBRE VALEURS MANQUANTES TOTALES : {vaManquante}\n"
      f"Pourcentage : {calc(vaManquante):.2f}\n"
      f"--------------------------------\n"
      f"NOMBRE VALEURS MANQUANTES (Col 6 et 7): {vaManquanteCol}\n"
      f"Pourcentage : {calc(vaManquanteCol):.2f}\n"
      f"--------------------------------\n"
      f"NOMBRE VALEURS ABERANTES (Col 6 et 7): {vaAberante}\n"
      f"Pourcentage : {calc(vaAberante):.2f}\n"
      f"--------------------------------\n"
      f"Total d'erreur (Col 6 et 7): {total}\n"
      f"Pourcentage d'erreur total : {calc(total):.2f}\n"
      f"--------------------------------\n"
      f"SEUL LES COLONNES 6 ET 7 ONT ÉTÉ CORRIGÉ DANS LE FICHIER FINAL")

