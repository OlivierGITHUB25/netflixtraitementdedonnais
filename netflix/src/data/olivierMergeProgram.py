import pandas as pds
import pandas as pd
import os
from pandas import DataFrame

#output = pd.concat(
    #map(pd.read_csv, ['netflix-1.csv', 'netflix-2.csv','netflix-3.csv','netflix-4.csv','netflix-5.csv' ]), ignore_index=True)

#output.to_csv("fusion.csv", index=False)
#df = DataFrame.from_items(
 #   orient='index',
  #  columns=['show_id','type','title','director','cast','country','date_added','release_year','rating','duration','listed_in','description'])
#del df['description']
for i in range (1,6):
    lecture= pds.read_csv(f"../../data/raw/netflix-{i}.csv", header=None)
    test = lecture.drop(lecture.columns[11], axis=1)
df = pd.concat(
    map(pd.read_csv, ['../../output/output1.csv', '../../output/output2.csv','../../output/output3.csv','../../output/output4.csv','../../output/output5.csv']), ignore_index=True)
df.to_csv("../../output/merge.csv", index=False)