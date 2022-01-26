import pandas
import pandas as pd

read = pd.read_csv('fusion.csv', index_col=False)
valeurManquante = 0
valeurAberante = 0


for i in range(1, 8808):
    added = read.iloc[i, 6]
    released = int(read.iloc[i, 7])
    try:
        nothing, added = added.split(",")
        added = int(added)
    except:
        print(f"ERREUR VALEUR s{i}")
        valeurManquante += 1

    if added < released:
        valeurAberante += 1
        print(added, released, f"--> Erreur Ligne s{i}")


valeurManquante_ = valeurManquante * 100 / 8808
valeurAberante_ = valeurAberante * 100 / 8808
total = valeurAberante + valeurManquante
total_ = total * 100 / 8808


print(f"--------------------------------\n"
      f"NOMBRE VALEURS MANQUANTES : {valeurManquante}\n"
      f"Pourcentage : {valeurManquante_:.2f}\n"
      f"--------------------------------\n"
      f"NOMBRE VALEURS ABERANTES : {valeurAberante}\n"
      f"Pourcentage : {valeurAberante_:.2f}\n"
      f"--------------------------------\n"
      f"Total d'erreur : {total}\n"
      f"Pourcentage d'erreur total : {total_:.2f}")