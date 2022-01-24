import pandas as pd
import glob
import os

joined_files = os.path.join("netflix-*.csv")

joined_list = glob.glob(joined_files)

# Finally, the files are joined
df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
print(df)

output=(df)
output.to_csv("test.csv",index=False)