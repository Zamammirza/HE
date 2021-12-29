import pandas as pd

from brisque_calculation import calculate_brisque

import utils
import os

df = pd.DataFrame(columns=["algorithm", "original_filename", "score"])

algorithms = os.listdir("processed")
for algorithm in algorithms:
    counter = 1
    for filename in os.listdir(f"processed/{algorithm}"):
        original_filename = filename.removesuffix(f"_{algorithm}.png") + ".png"

        print(f"{counter} scoring {algorithm}/{original_filename}")

        image = utils.load(filename, "processed/" + algorithm)
        score = calculate_brisque(image)

        print(f"got {score}")

        df.loc[len(df)] = [algorithm, original_filename, score]

        counter += 1
print(df)

# create output folder if it doesn't exist
output_folder = "results"
if not os.path.isdir(output_folder):
    os.makedirs(output_folder)

output_path = "results/brisque_scores.csv"
df.to_csv("results/brisque_scores.csv", index_label=False, index=False)
print(f"\nwrote to {output_path}\n")