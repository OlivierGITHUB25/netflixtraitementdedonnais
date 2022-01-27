import pandas as pd

for i in range (1, 6):
    read = pd.read_csv(f"../../data/raw/netflix-{i}.csv", header=None)
    read = read.drop(read.columns[11], axis=1)
    read.to_csv(f"../../output/output{i}.csv", index=False)

df = pd.concat(
    map(pd.read_csv, ['../../output/output1.csv', '../../output/output2.csv','../../output/output3.csv','../../output/output4.csv','../../output/output5.csv']),
    ignore_index=True)

df.to_csv("../../output/merge.csv", index=False)
