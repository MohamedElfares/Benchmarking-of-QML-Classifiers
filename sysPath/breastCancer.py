from summarize import getTopFeatures



# Pre-process the dataset & feature engineering
def preProcessing(dataset, classMap):
    dataset = dataset.dropna() # drop NaN values
    dataset = dataset.reset_index(drop = True) # reset the indices

    # split the dataset into features & class
    features = dataset.copy(deep=True)
    features = features.drop(["id", "diagnosis"], axis = 1)
    
    labels = dataset[["diagnosis"]].copy(deep=True)
    labels["diagnosis"] = labels["diagnosis"].map(classMap)

    # Retrieve the top 5 significant features
    topFeauters = getTopFeatures(features, labels, 5)
    features = features[topFeauters].copy(deep=True)

    return features, labels