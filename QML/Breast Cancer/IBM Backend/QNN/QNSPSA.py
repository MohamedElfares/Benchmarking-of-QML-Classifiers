import os
import gc
import sys
import time

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
modelName = "QNSPSA"

# Set up file paths and directories
sysPath = r"../../../../sysPath"
sys.path.append(sysPath)
os.chdir(dname)

with open(f"{sysPath}/API.txt", "r") as file:
    API = file.read()

base_dir = os.path.join(dname, rf"{modelName}")
models_dir = os.path.join(dname, rf"{modelName}/Trained Models")
results_dir = os.path.join(dname, rf"{modelName}/Results")

if not os.path.exists(base_dir):
    os.makedirs(base_dir)
if not os.path.exists(models_dir):
    os.makedirs(models_dir)
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

from qiskit import QuantumCircuit
from qiskit_algorithms.optimizers import QNSPSA
from qiskit.circuit.library import RealAmplitudes, TwoLocal
from qiskit.circuit.library import ZFeatureMap, ZZFeatureMap, PauliFeatureMap

from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler

from qiskit_machine_learning.neural_networks import SamplerQNN
from qiskit_machine_learning.algorithms.classifiers import NeuralNetworkClassifier as classifier

from summarize import display, recordResult, saveFig, recordXLSX, barPlot # type: ignore
from summarize import getTopFeatures, prepData, modelEvaluation, lastTouch # type: ignore

import logging
import pandas as pd

logging.basicConfig()
firstPhase = time.time()


optimizer = QNSPSA()
classMap = {"M": -1, "B": 1}
smoteStatus = False

service = QiskitRuntimeService(channel = "ibm_quantum", token = API)
session = Session(service = service, backend = "ibmq_qasm_simulator")
sampler = Sampler(session = session)



# Pre-process the dataset & feature engineering
def preProcessing(dataset):
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



# Load dataset
print("Dataset before pre-Processing")
print("="*20)
dataset = pd.read_csv(r"../../../../Datasets/Breast Cancer.csv")
print(dataset.info())
features, labels = preProcessing(dataset.copy(deep=True))
print("\n\nDataset after pre-Processing")
print("="*20)
print(features.info())



ratio = labels["diagnosis"].value_counts()[1] / len(labels) # get the ratio of the dataset (B:M)
smoteStatus = False if 0.45 <= ratio <= 0.55 else True # Apply SMOTE for data balancing if the ratio is outside the range 40%-60%.
dataTrain, dataTest, labelsTrain, labelsTest, n_qubits = prepData(features, labels, smoteStatus)
data = pd.DataFrame(columns=["Model Name", "FeatureMap", "Anstaz", "# Qubits" "# M", "# B",  "B:M", "Smote", "Precision-Score", "Recall-Score", "F1-Score", "Accuracy"])




# set the configs which is the test name along with it's combination of the cofactors.
configs = [
    {
        "TestName": "Test 1",
        "Test": {
            "featureMap_Name": "ZFeatureMap",
            "FeatureMap": ZFeatureMap(feature_dimension = n_qubits),
            "anstaz_Name": "RealAmplitudes",
            "ansatz": RealAmplitudes(num_qubits= n_qubits, entanglement="full")
        }
    },

    {
        "TestName": "Test 2",
        "Test": {
            "featureMap_Name": "ZZFeatureMap",
            "FeatureMap": ZZFeatureMap(feature_dimension = n_qubits),
            "anstaz_Name": "RealAmplitudes",
            "ansatz": RealAmplitudes(num_qubits = n_qubits, entanglement="full")
        }
    },

    {
        "TestName": "Test 3",
        "Test": {
            "featureMap_Name": "PauliFeatureMap",
            "FeatureMap": PauliFeatureMap(feature_dimension = n_qubits),
            "anstaz_Name": "RealAmplitudes",
            "ansatz": RealAmplitudes(num_qubits= n_qubits, entanglement="full")
        }
    },

    {
        "TestName": "Test 4",
        "Test": {
            "featureMap_Name": "ZFeatureMap",
            "FeatureMap": ZFeatureMap(feature_dimension = n_qubits),
            "anstaz_Name": "TwoLocal",
            "ansatz": TwoLocal(num_qubits = n_qubits, rotation_blocks = ["rx", "rz"], entanglement_blocks = "cx")
        }
    },

    {
        "TestName": "Test 5",
        "Test": {
            "featureMap_Name": "ZZFeatureMap",
            "FeatureMap": ZZFeatureMap(feature_dimension = n_qubits),
            "anstaz_Name": "TwoLocal",
            "ansatz": TwoLocal(num_qubits = n_qubits, rotation_blocks = ["rx", "rz"], entanglement_blocks = "cx")
        }
    },

    {
        "TestName": "Test 6",
        "Test": {
            "featureMap_Name": "PauliFeatureMap",
            "FeatureMap": PauliFeatureMap(feature_dimension = n_qubits),
            "anstaz_Name": "TwoLocal",
            "ansatz": TwoLocal(num_qubits = n_qubits, rotation_blocks = ["rx", "rz"], entanglement_blocks = "cx")
        }
    }
]



# Record the elapsed time for pre-processing and feature engineering phase
firstPhase = time.time() - firstPhase



for config in configs:
    secondPhase = time.time()

    testName = config["TestName"]
    test = config["Test"] # Get the Test dictionary.

    # Retrieve details for the test.
    ansatz = test["ansatz"]
    feature_map = test["FeatureMap"]
    anstaz_Name = test["anstaz_Name"]
    featureMap_Name = test["featureMap_Name"]

    print(f"\n\n{testName}")
    print("="*len(testName))

    # Set up quantum cirquit and fit the model.
    qc = QuantumCircuit(n_qubits)
    qc = qc.compose(feature_map)
    qc = qc.compose(ansatz)
    
    neural_network = SamplerQNN(circuit=qc, sampler=sampler, input_params=feature_map.parameters, weight_params=ansatz.parameters)

    model = classifier(neural_network, optimizer=optimizer)
    model.fit(dataTrain, labelsTrain)
    model.save(rf"{models_dir}/{testName}.model") # Save the model

    # Record the elapsed time for training phase
    secondPhase = time.time() - secondPhase
    executionTime = firstPhase + secondPhase

    # Evaluate model, display results, record, and save figures that include scores, classification report, and confusion matrices.
    predicted, precision, accuracy, recall, f1, classificationReport = modelEvaluation(model, dataTest, labelsTest, list(classMap.keys()))
    saveFig(results_dir, labelsTest, predicted, accuracy, testName)
    display(featureMap_Name, anstaz_Name, n_qubits, ratio, smoteStatus, executionTime, classificationReport)
    recordResult(base_dir, testName, featureMap_Name, anstaz_Name, n_qubits, ratio, smoteStatus, executionTime, classificationReport)

    # summarize the configs & results into an excel file for readability.
    MCount = len(dataset[dataset.diagnosis == "M"])
    BCount = len(dataset[dataset.diagnosis == "B"])
    recordXLSX(data, modelName, featureMap_Name, anstaz_Name, n_qubits, MCount, BCount, ratio, smoteStatus, precision, recall, f1, accuracy)

    gc.collect()

# plot the results of each combination of config based on Accuracy & F1-Score to easily comparison
barPlot(data, base_dir)
data.to_excel(rf"{base_dir}/summary.xlsx", index = False)
lastTouch(base_dir)