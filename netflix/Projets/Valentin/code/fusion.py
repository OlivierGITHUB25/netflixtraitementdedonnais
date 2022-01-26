import pandas as pd
import os

for i in range (1, 6):
    read = pd.read_csv(f"../../../data/raw/netflix-{i}.csv", header=None)
    read = read.drop(read.columns[11], axis=1)
    read.to_csv(f"output{i}.csv", index=False)

df = pd.concat(
    map(pd.read_csv, ['output1.csv', 'output2.csv','output3.csv','output4.csv','output5.csv']),
    ignore_index=True)

df.to_csv("fusion.csv", index=False)

for i in range (1, 6):
    os.remove(f"output{i}.csv")