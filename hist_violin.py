import sys
import matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('results/brisque_scores.csv')

# df["score"] =  df["score"].round(decimals = 2)

# print(df)

# for x in df.index:
#   if df.loc[x, "score"] == 0:
#     df.drop(x, inplace = True)
#     df.to_csv("results/brisque_scores_empty.csv", index_label=False, index=False)



no_processing = df[df["algorithm"] == "no_processing"]
bbhe = df[df["algorithm"] == "bbhe"]
# bbhe = df[df["score"] < 55]
clahe = df[df["algorithm"] == "clahe"]
splinet = df[df["algorithm"] == "splinet"]




print(bbhe, splinet, no_processing, clahe)
x=[ no_processing["score"], bbhe["score"], clahe["score"], splinet["score"]]
# labels=[ "no_processing", "BBHE", "CLAHE", "SpliNet"]


fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(3.3, 2.1))

axs.tick_params(axis='both', which='major', labelsize=8)

# axs[0].hist(x, histtype='bar', stacked=False, fill=True, label=labels)
# axs[0].set_title('Histogram')
# axs[0].legend()
# # axs[0].set_xlabel('BRISQUE Score\n\n Figure (1): Histogram BRISQUE score values for different\nHistogram Equalization algorithms')
# axs[0].set_ylabel('Frequency')




axs.violinplot(x, showmedians=True)
# axs.set_title('Violin Plot')
axs.set_xticks([1,2,3,4])
axs.set_xticklabels(["No Processing", "BBHE", "CLAHE", "SpliNet"])
# axs[1].set_xlabel('Algorithms\n\n Figure (2): violin plot for each Histogram Equalization algorithm\n dataset with median marker line')
axs.set_ylabel('BRISQUE Score', fontsize=8)


plt.grid(which="major", zorder=0)
plt.grid(which="minor", linestyle=":", linewidth=.4, zorder=0)


fig.tight_layout(pad=1)

# txt="Figure (X):"
# plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12)


plt.savefig("violin.pdf")

plt.show()