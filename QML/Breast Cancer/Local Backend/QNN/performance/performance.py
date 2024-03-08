import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)

# Set up file paths and directories
sys.path.append(r"../../../../sysPath")
os.chdir(dname)
os.chdir("../")
current_path = os.getcwd()



def barplot(data):
    modelName = data["Model Name"].tolist()
    FeatureMap = data["FeatureMap"].tolist()
    Anstaz = data["Anstaz"].tolist()

    # Combine FeatureMap and Anstaz names to create custom x-axis tick labels
    configs = [f'{md}\n{fm}\n{ans}' for md, fm, ans in zip(modelName, FeatureMap, Anstaz)]

    measures = {
        "Accuracy": data["Accuracy"].tolist(),
        "F1-score":  data["F1-Score"].tolist()
    }

    x = np.arange(len(data.index))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots(figsize=(12, 8))

    for idx, (attribute, measurement) in enumerate(measures.items()):
        rects = ax.bar(x + (idx * width), measurement, width, label=attribute)
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.2f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("Percentage (%)")
    ax.set_title("Comparison of model performance.")
    ax.set_xticks(x + width/2)
    ax.set_xticklabels(configs)
    ax.legend()

    plt.tight_layout()
    plt.savefig(f"performance/best Performance.png", dpi=1000)
    plt.close()



performance = pd.DataFrame()

ignore = ["performance"]
folders = [folder for folder in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, folder)) and folder not in ignore]

for folder in folders:
    candidate = pd.read_excel(f"{current_path}/{folder}/summary.xlsx")

    candidate["Primary Factor"] = candidate["F1-Score"] + candidate["Accuracy"]
    candidate = candidate[candidate["Primary Factor"] == candidate["Primary Factor"].max()]

    candidate["Secondary Factor"] = candidate["Primary Factor"] + candidate["Execution Time (s)"]
    candidate = candidate[candidate["Secondary Factor"] == candidate["Secondary Factor"].min()]

    candidate = candidate.reset_index(drop=True)
    candidate = candidate.drop(columns=["Primary Factor", "Secondary Factor"])

    performance = pd.concat([performance, candidate])


performance.reset_index(drop=True, inplace=True)
barplot(performance)