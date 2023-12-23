import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score



def getTopFeatures(features, target, nFeautres = 5):
    best_features = SelectKBest(score_func = chi2, k = nFeautres)
    fit = best_features.fit(features, target)

    top_feature_indices = fit.get_support(indices=True)  # Get the indices of the top k features
    top_feature_names = features.columns[top_feature_indices] # Get the names of the top k features

    return top_feature_names.tolist()



def get_optimal_components(X_train):
    pca = PCA().fit(X_train)  # Fit PCA on training data
    explained_variance = np.cumsum(pca.explained_variance_ratio_)

    # Find the optimal number of components based on the graph
    optimal_components = np.argmax(explained_variance >= 0.95) + 1  # Adjust threshold as needed
    optimal_components = 2 if optimal_components == 1 else optimal_components
    return optimal_components



def setPCA(X_train, X_test):
    n_components = get_optimal_components(X_train)
    pca = PCA(n_components = n_components).fit(X_train)
    X_train = pca.transform(X_train)
    X_test = pca.transform(X_test)

    return X_train, X_test, n_components



def smote(X_train, y_train):
    sm = SMOTE()
    X_train, y_train = sm.fit_resample(X_train, y_train) # type: ignore
    return X_train, y_train



def prepData(features, labels, smote_Status):
    X_train, X_test, y_train, y_test = train_test_split(features.to_numpy(), labels.to_numpy(), test_size = 0.20, random_state = 42)
    
    if smote_Status:
        X_train, y_train = smote(X_train, y_train)

    # Normalize
    std_scale = StandardScaler().fit(X_train)
    X_train = std_scale.transform(X_train)
    X_test = std_scale.transform(X_test)

    # Scale for better fit within the feature map
    minmax_scale = MinMaxScaler().fit(X_train)
    X_train = minmax_scale.transform(X_train)
    X_test = minmax_scale.transform(X_test)

    X_train, X_test, n_components = setPCA(X_train, X_test)

    return X_train, X_test, y_train, y_test, n_components



def modelEvaluation(model, X_test, y_test, target_names):
    predicted = np.round(model.predict(X_test))

    precision = precision_score(y_test, predicted)
    accuracy = accuracy_score(y_test, predicted)
    recall = recall_score(y_test, predicted)
    f1 = f1_score(y_test, predicted)

    classificationReport = classification_report(y_test, predicted, target_names = target_names)

    return predicted, precision, accuracy, recall, f1, classificationReport



def display(featureMap_Name, anstaz_Name, n_qubits, ratio, smoteStatus, time, classificationReport):
    print()
    print(f"ansatz used:            {anstaz_Name}")
    print(f"featureMap used:        {featureMap_Name}")
    print(f"# Qubits used:          {n_qubits}")
    print(f"Ratio:                  {ratio:.2f}:{(1-ratio):.2f}")
    print(f"SMOTE:                  {smoteStatus}")
    print(f"Execution Time:         {int(time)}s\n")
    print(classificationReport) # type: ignore
    print("_"*100 + "\n")


def display_Override(featureMap_Name, ratio, n_qubits, smoteStatus, time, classificationReport):
    print()
    print(f"featureMap used:        {featureMap_Name}")
    print(f"# Qubits used:          {n_qubits}")
    print(f"Ratio:                  {ratio:.2f}:{(1-ratio):.2f}")
    print(f"SMOTE:                  {smoteStatus}")
    print(f"Execution Time:         {int(time)}s\n")
    print(classificationReport) # type: ignore
    print("_"*100 + "\n")



def recordResult(path, testName, featureMap_Name, anstaz_Name, n_qubits, ratio, smoteStatus, time, classificationReport):
    recordName = rf"{path}/Description.md"
    with open(recordName, "a") as descriptionFile:
        descriptionFile.write(f"\n## {testName}\n")
        descriptionFile.write("### Configurations:\n")
        descriptionFile.write("<pre>\n")
        descriptionFile.write(f"  ansatz used:          {anstaz_Name}\n")
        descriptionFile.write(f"  featureMap used:      {featureMap_Name}\n")
        descriptionFile.write(f"  # Qubits used:        {n_qubits}\n")
        descriptionFile.write(f"  Ratio:                {ratio:.2f}:{(1-ratio):.2f}\n")
        descriptionFile.write(f"  SMOTE:                {smoteStatus}\n")
        descriptionFile.write(f"  Execution Time:       {int(time)}s\n")
        descriptionFile.write("</pre>\n")
        descriptionFile.write("\n<br>\n<br>\n")
        descriptionFile.write("\n### Results Summary:\n")
        descriptionFile.write("<pre>\n")
        descriptionFile.write(classificationReport)  # type: ignore
        descriptionFile.write("</pre>\n\n")
        descriptionFile.write(f"<img src='Results/{testName}.png' alt='{testName}.png' width=50% height=50%>\n")
        descriptionFile.write("\n---\n\n")
        descriptionFile.write("<br>\n<br>\n")



def recordResult_Override(path, testName, featureMap_Name, n_qubits, ratio, smoteStatus, time, classificationReport):
    recordName = rf"{path}/Description.md"
    with open(recordName, "a") as descriptionFile:
        descriptionFile.write(f"\n## {testName}\n")
        descriptionFile.write("### Configurations:\n")
        descriptionFile.write("<pre>\n")
        descriptionFile.write(f"  featureMap used:      {featureMap_Name}\n")
        descriptionFile.write(f"  # Qubits used:        {n_qubits}\n")
        descriptionFile.write(f"  Ratio:                {ratio:.2f}:{(1-ratio):.2f}\n")
        descriptionFile.write(f"  SMOTE:                {smoteStatus}\n")
        descriptionFile.write(f"  Execution Time:       {int(time)}s\n")
        descriptionFile.write("</pre>\n")
        descriptionFile.write("\n<br>\n<br>\n")
        descriptionFile.write("\n### Results Summary:\n")
        descriptionFile.write("<pre>\n")
        descriptionFile.write(classificationReport)  # type: ignore
        descriptionFile.write("</pre>\n\n")
        descriptionFile.write(f"<img src='Results/{testName}.png' alt='{testName}.png' width=50% height=50%>\n")
        descriptionFile.write("\n---\n\n")
        descriptionFile.write("<br>\n<br>\n")



def saveFig(path, y_test, predicted, accuracy, testName):
    confusionMatrix = confusion_matrix(y_test, predicted)

    ax = plt.subplot()
    sns.heatmap(confusionMatrix, annot = True, fmt = 'g', ax = ax, cmap = "viridis") # annot = True to annotate cells, ftm = 'g' to disable scientific notation

    # labels, title and ticks
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title(f"Accuracy: {accuracy*100:.2f}%")
    ax.xaxis.set_ticklabels(["M", "B"])
    ax.yaxis.set_ticklabels(["M", "B"])

    plt.savefig(f"{path}/{testName}.png", dpi = 1000)
    plt.close()



def recordXLSX(data, modelName, featureMap_Name, anstaz_Name, n_qubits, falseCount, trueCount, ratio, smote_state, precision, recall, f1, accuracy):
    data.loc[len(data.index)] = [modelName, featureMap_Name, anstaz_Name, n_qubits, falseCount, trueCount, ratio, smote_state, precision, recall, f1, accuracy] # type: ignore



def recordXLSX_Override(data, modelName, featureMap_Name, n_qubits, falseCount, trueCount, ratio, smote_state, precision, recall, f1, accuracy):
    data.loc[len(data.index)] = [modelName, featureMap_Name, n_qubits, falseCount, trueCount, ratio, smote_state, precision, recall, f1, accuracy] # type: ignore



def barPlot(data, path):
    FeatureMap = data["FeatureMap"].tolist()
    Anstaz = data["Anstaz"].tolist()

    # Combine FeatureMap and Anstaz names to create custom x-axis tick labels
    configs = [f'{fm}\n{ans}' for fm, ans in zip(FeatureMap, Anstaz)]

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
    plt.savefig(f"{path}/Performance.png", dpi=1000)
    plt.close()



def barPlot_Override(data, path):
    FeatureMap = data["FeatureMap"].tolist()

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
    ax.set_xticklabels(FeatureMap)
    ax.legend()

    plt.tight_layout()
    plt.savefig(f"{path}/Performance.png", dpi=1000)
    plt.close()



def lastTouch(path):
    recordName = rf"{path}/Description.md"
    with open(recordName, "a") as descriptionFile:
        descriptionFile.write(f"\n<img src='Performance.png' alt='Performance.png'>\n")