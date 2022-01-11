import sys
import matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('results/brisque_scores.csv')

# df["score"] =  df["score"].round(decimals = 2)

# print(df)

for x in df.index:
  if df.loc[x, "score"] == 0:
    df.drop(x, inplace = True)
    df.to_csv("results/brisque_scores_empty.csv", index_label=False, index=False)


bbhe = df[df["algorithm"] == "bbhe"]
# bbhe = df[df["score"] > 55]
splinet = df[df["algorithm"] == "splinet"]
no_processing = df[df["algorithm"] == "no_processing"]
clahe = df[df["algorithm"] == "clahe"]



print(bbhe, splinet, no_processing, clahe)
x=[bbhe["score"], splinet["score"], no_processing["score"], clahe["score"]]
labels=["bbhe", "splinet", "no_processing", "clahe"]
plt.hist(x, histtype='bar', stacked=False, fill=True, label=labels)
plt.legend()

# plt.savefig("fig.pdf")



# print(df)

# print(df.to_string())
# df.plot()

# print(df.info()) 

# df.plot(x = 'algorithm', y = 'score', rot=10)

# df["score"].plot(kind = 'hist', x = 'score')

# plt.bar(bbhe)
plt.show()

# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()