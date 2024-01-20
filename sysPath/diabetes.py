import warnings
import numpy as np
import pandas as pd

from summarize import getTopFeatures
from sklearn.impute import KNNImputer
from sklearn.preprocessing import MinMaxScaler

warnings.filterwarnings("ignore", category=FutureWarning)



def Outlier(dataset, col_name):
    Q1 = 0.25
    Q3 = 0.75

    p25 = dataset[col_name].quantile(Q1)
    p75 = dataset[col_name].quantile(Q3)

    IQR = p75 - p25
    up_limit = p75 + 1.5 * IQR
    low_limit = p25 - 1.5 * IQR

    return low_limit, up_limit



def fixOutlier(dataset, features):
    for feature in features:
        low_limit, up_limit = Outlier(dataset, feature)
        dataset.loc[(dataset[feature] < low_limit), feature] = low_limit
        dataset.loc[(dataset[feature] > up_limit), feature] = up_limit

    dataset = dataset.reset_index()
    dataset.head()
    return dataset



def fixFeautres(dataset, features):
    scaler = MinMaxScaler()
    imputer = KNNImputer(n_neighbors = 5)

    dataset = pd.get_dummies(dataset[features], drop_first = True)
    dataset = pd.DataFrame(scaler.fit_transform(dataset), columns = features)
    dataset = pd.DataFrame(imputer.fit_transform(dataset), columns = features)
    dataset = pd.DataFrame(scaler.inverse_transform(dataset), columns= features)

    return dataset[features]



def Age_CAT(dataset, feature):
    classMap = {"young_women": 0, "mature_women": 1, "middle_age": 2, "old_age": 3, "elder_age": 4}
    
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 18) & (pd.to_numeric(dataset[feature], errors='coerce') < 30) , feature] = "young_women"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 30) & (pd.to_numeric(dataset[feature], errors='coerce') < 45) , feature] = "mature_women"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 45) & (pd.to_numeric(dataset[feature], errors='coerce') < 65) , feature] = "middle_age"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 65) & (pd.to_numeric(dataset[feature], errors='coerce') < 75) , feature] = "old_age"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 75) , feature] = "elder_age"

    return dataset[feature].map(classMap)



def BMI_CAT(dataset, feature):
    classMap = {"overweak": 0, "weak": 1, "normal": 2, "overweight": 3, "1st_Obese": 4, "2nd_Obese": 5, "3rd_Obese": 6}

    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') < 16), feature] = "overweak"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 16) & (pd.to_numeric(dataset[feature], errors='coerce') < 18.5) , feature] = "weak"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 18.5) & (pd.to_numeric(dataset[feature], errors='coerce') < 25) , feature] = "normal"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 25) & (pd.to_numeric(dataset[feature], errors='coerce') < 30) , feature] = "overweight"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 30) & (pd.to_numeric(dataset[feature], errors='coerce') < 35) , feature] = "1st_Obese"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 35) & (pd.to_numeric(dataset[feature], errors='coerce') < 45) , feature] = "2nd_Obese"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 45), feature] = "3rd_Obese"

    return dataset[feature].map(classMap)



def Glucose_CAT(dataset, feature):
    classMap = {"hipoglisemi": 0, "normal": 1, "imparied glucose": 2, "hiperglisemi": 3}

    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') < 70), feature] ="hipoglisemi"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 70) & (pd.to_numeric(dataset[feature], errors='coerce') < 100) , feature] ="normal"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 100) & (pd.to_numeric(dataset[feature], errors='coerce') < 126) , feature] ="imparied glucose"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 126), feature] ="hiperglisemi"

    return dataset[feature].map(classMap)



def Insulin_CAT(dataset, feature):
    classMap = {"normal": 0, "abnormal": 1}

    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') < 120)  , feature] = "normal"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 120) , feature] = "abnormal"

    return dataset[feature].map(classMap)



def Pregnancies_CAT(dataset, feature):
    classMap = {"unpregnant": 0, "normal": 1, "high": 2, "very high": 3}

    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') == 0)  , feature] = "unpregnant"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') > 0 ) & (pd.to_numeric(dataset[feature], errors='coerce') <= 5)  , feature] = "normal"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') > 5 ) & (pd.to_numeric(dataset[feature], errors='coerce') <= 10 )  , feature] = "high"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') > 10 )  , feature] = "very high"

    return dataset[feature].map(classMap)



def BloodPressure_CAT(dataset, feature):
    classMap = {"low": 0, "normal": 1, "high": 2}

    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') < 70)  , feature] = "low"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 70) & (pd.to_numeric(dataset[feature], errors='coerce') < 90) , feature] = "normal"
    dataset.loc[(pd.to_numeric(dataset[feature], errors='coerce') >= 90 ) , feature] = "high"

    return dataset[feature].map(classMap)



def numeric_To_category(dataset):
    dataset["Age"] = Age_CAT(dataset.copy(deep=True), "Age")
    dataset["BMI"] = BMI_CAT(dataset.copy(deep=True), "BMI")
    dataset["Glucose"] = Glucose_CAT(dataset.copy(deep=True), "Glucose")
    dataset["Insulin"] = Insulin_CAT(dataset.copy(deep=True), "Insulin")
    dataset["Pregnancies"] = Pregnancies_CAT(dataset.copy(deep=True), "Pregnancies")
    dataset["BloodPressure"] = BloodPressure_CAT(dataset.copy(deep=True), "BloodPressure")
    
    return dataset



# Pre-process the dataset & feature engineering
def preProcessing(dataset):
    # list features that need to be Engineered
    corruptedFeatures = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    refineFeatures_list = ["Insulin", "SkinThickness"]

    # replace non-sense values with NaN to easly deel with it
    dataset[corruptedFeatures] = dataset[corruptedFeatures].replace(0, np.NaN)
    dataset = fixOutlier(dataset.copy(deep=True), dataset.columns)

    # fill NaN values with median for low percentage (missing values).
    dataset["Glucose"] = dataset["Glucose"].fillna(dataset["Glucose"].median())
    dataset["BloodPressure"] = dataset["BloodPressure"].fillna(dataset["BloodPressure"].median())
    dataset["BMI"] = dataset["BMI"].fillna(dataset["BMI"].median())

    # deal with heigh percentage (missing values) with other way.
    fixedFeatures = fixFeautres(dataset.copy(deep=True), refineFeatures_list)
    for feature in fixedFeatures.columns:
        dataset[[feature]] = fixedFeatures[[feature]]

    # # convert the continues numeric variable to categorical values then map them to numirical
    # dataset = numeric_To_category(dataset.copy(deep=True))
    if "index" in dataset.columns: dataset.drop(["index"], axis = 1, inplace = True)

    # split the dataset into features & class
    features = dataset.copy(deep=True)
    features = features.drop(["Outcome"], axis = 1)
    labels = dataset[["Outcome"]].copy(deep=True)

    # Retrieve the top 5 significant features
    topFeauters = getTopFeatures(features, labels, 5)
    features = features[topFeauters].copy(deep=True)
    
    return features, labels