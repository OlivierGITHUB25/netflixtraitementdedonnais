import csv

with open('output.csv', 'w', newline='', encoding="utf8") as output:
    for i in range(1, 6):
        with open(f'../../../data/raw/netflix-{i}.csv', newline='', encoding="utf8") as csvFile:
            for row in csvFile:
                ecriture = csv.writer(output)
                ecriture.writerow(csvFile)

