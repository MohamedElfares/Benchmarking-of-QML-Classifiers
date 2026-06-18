# Quantum Machine Learning — Benchmarking QSVM & VQC for Binary Classification

> Research project from the **University of Sharjah** benchmarking Quantum Support Vector Machines (QSVM) and Variational Quantum Circuits (VQC) against classical classifiers on binary classification tasks.

---

## Overview

Classical machine learning algorithms face well-known computational limits on high-dimensional data. Quantum Machine Learning (QML) exploits **superposition** and **entanglement** to process information in parallel, opening the door to exponential speedup on certain tasks.

This project trains and evaluates quantum classifiers on three real-world datasets — Breast Cancer, Diabetes, and Titanic — across **100+ test configurations** that vary the feature map, ansatz, optimizer, and data preprocessing settings. All experiments run on a quantum simulator using [Qiskit](https://qiskit.org/).

**Paper:** *Benchmarking of Quantum Support Vector Machine and Variational Quantum Circuit with Binary Classification* — Mohamed Aly, Manar Abu Talib, Salma Fadaaq, Qassim Nasir — University of Sharjah.

---

## Table of Contents

1. [Pipeline Architecture](#pipeline-architecture)
2. [Quantum Components](#quantum-components)
3. [Classifiers](#classifiers)
4. [Datasets](#datasets)
5. [Test Configurations](#test-configurations)
6. [Key Findings](#key-findings)
7. [Repository Structure](#repository-structure)
8. [Requirements](#requirements)
9. [Installation](#installation)
10. [Usage](#usage)

---

## Pipeline Architecture

Every experiment follows the same eight-stage pipeline:

```
Raw Dataset
    │
    ▼
┌─────────────────────────────┐
│  1. Dimensionality Reduction │  PCA → n components
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  2. Data Normalization       │  StandardScaler
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  3. Data Scaling             │  MinMaxScaler → [0, 1]
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  4. Class Balancing          │  SMOTE (if class ratio < 45% or > 55%)
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  5. Feature Map              │  Encode classical bits → qubits
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  6. Parameterized Circuit    │  Ansatz (trainable quantum layers)
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  7. Optimizer                │  Minimize objective function
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  8. Sampler / Classifier     │  Measure → classify → evaluate
└─────────────────────────────┘
```

### Stage Details

**Dimensionality Reduction — PCA**
PCA reduces the feature space before encoding into qubits. Most experiments use `n_components = 2` (2 qubits). A subset of specialized tests uses `n_components = 5`, which increases training time by 1.5–2× but can improve accuracy.

**Data Normalization — StandardScaler**
Standardizes features to zero mean and unit variance, ensuring no single feature dominates the quantum encoding.

**Data Scaling — MinMaxScaler**
Rescales normalized features to [0, 1], a required range for angle-based quantum encoding in feature maps.

**Class Balancing — SMOTE**
SMOTE is applied automatically when the minority-to-majority class ratio falls outside the 45%–55% range.

---

## Quantum Components

### Feature Maps

Feature maps encode classical data into quantum states. Three feature maps are tested:

| Feature Map | Complexity | Description |
|---|---|---|
| `ZFeatureMap` | Low | Single-qubit Z-rotations; fastest training |
| `ZZFeatureMap` | Medium | Adds ZZ-interaction terms between qubits |
| `PauliFeatureMap` | High | Generalizes to arbitrary Pauli operators |

`ZFeatureMap` is the most stable across different ansatz types, consistently producing high accuracy with shorter training times. `ZZFeatureMap` and `PauliFeatureMap` can match its accuracy but are more sensitive to the choice of ansatz and preprocessing.

### Ansatz (Parameterized Quantum Circuits)

The ansatz acts like the trainable layers of a classical neural network. Two options are tested:

| Ansatz | Rotation Blocks | Entanglement |
|---|---|---|
| `RealAmplitudes` | Ry | Configurable (full, linear, circular, etc.) |
| `TwoLocal` | Rx + Rz | CX gates |

`TwoLocal` showed irregular behavior (abnormal accuracy or training time) across multiple optimizers. `RealAmplitudes` with `full` entanglement was more reliable overall.

### Optimizers

Six optimizers are benchmarked for training speed and accuracy:

| Optimizer | Training Speed | Accuracy | Notes |
|---|---|---|---|
| `ADAM` | Slow (> 8 hrs at high dims) | High | Gradient-based; consistent results |
| `L_BFGS_B` | Fast (minutes) | High | Recommended for most cases |
| `SLSQP` | Fast (minutes) | High | Recommended for most cases |
| `COBYLA` | Fast (minutes) | Moderate | Gradient-free; good baseline |
| `AQGD` | Moderate (1–2 hrs) | Variable | Quantum gradient descent |
| `QNSPSA` | Slow (> 8 hrs) | Variable | Second-order quantum optimizer |

**Recommendation:** `L_BFGS_B` and `SLSQP` offer the best trade-off between accuracy and speed. Use `ADAM` or `QNSPSA` only when training time is not a constraint.

### Sampler

All experiments use Qiskit's `Sampler` primitive, which simulates measurement outcomes from quantum circuits on a classical machine.

---

## Classifiers

Four quantum classifiers are evaluated:

| Classifier | Type | Notes |
|---|---|---|
| `VQC` | Variational Quantum Classifier | Primary classifier; hybrid quantum-classical |
| `NeuralNetworkClassifier` | Quantum Neural Network | Close results to VQC |
| `QSVC` | Quantum Support Vector Classifier | Kernel-based |
| `PegasosQSVC` | Pegasos QSVC | Online learning variant of QSVC |

All four classifiers produced similar accuracy on clean datasets. Differences became more pronounced when the feature map and ansatz combination changed.

---

## Datasets

| Dataset | Task | Classes | Challenge |
|---|---|---|---|
| **Breast Cancer** | Malignant vs. Benign | M / B | Class imbalance (SMOTE applied when needed) |
| **Diabetes** | Diabetic vs. Non-diabetic | 0 / 1 | Intertwined features (duplicate values across classes) |
| **Titanic** | Survived vs. Not survived | 0 / 1 | Intertwined features; missing data |

The **Intertwined** problem — where different classes share identical feature values — is the main obstacle in the Diabetes and Titanic datasets. No preprocessing technique tested fully resolved this overlap, which explains the abnormal results in some test configurations.

---

## Test Configurations

For each dataset and each optimizer, six combinations of feature map and ansatz are tested:

| Test | Feature Map | Ansatz |
|---|---|---|
| Test 1 | ZFeatureMap | RealAmplitudes |
| Test 2 | ZZFeatureMap | RealAmplitudes |
| Test 3 | PauliFeatureMap | RealAmplitudes |
| Test 4 | ZFeatureMap | TwoLocal |
| Test 5 | ZZFeatureMap | TwoLocal |
| Test 6 | PauliFeatureMap | TwoLocal |

**6 configs × 6 optimizers × 3 datasets = 108+ tests total.**

### Extended Testing (Results Phase)

For configurations that scored ≥ 0.70 accuracy within 30 minutes of training time, three additional test rounds are run:

- **Test 0** — Explore the effect of enabling/disabling normalization and scaling individually.
- **Tests 1–5** — Vary the ansatz entanglement type: `full`, `linear`, `reverse_linear`, `circular`, `sca`.
- **Tests X+ / X++** — Increase PCA dimension from 2 to 5; explore further preprocessing variants.

---

## Key Findings

- **Preprocessing is the single most impactful factor.** Properly preprocessed data produced high accuracy regardless of the classifier or optimizer chosen.

- **ZFeatureMap outperforms in stability.** Across all optimizers, it was the least affected by ansatz choice, and maintained consistent accuracy.

- **ADAM and QNSPSA are too slow for practical use** at higher PCA dimensions. `L_BFGS_B` and `SLSQP` are faster and nearly as accurate.

- **TwoLocal causes irregular results** across multiple optimizers. `RealAmplitudes` with full entanglement is the safer default.

- **Increasing PCA from 2 to 5** extends training time by 1.5–2× but can improve accuracy on cleaner datasets like Breast Cancer.

- **The Intertwined problem** in Diabetes and Titanic limits quantum classifiers as much as it limits classical ones — QML does not resolve inherently ambiguous data.

---

## Repository Structure

```
Quantum-ML/
├── Datasets/
│   ├── Breast Cancer.csv
│   ├── Diabetes.csv
│   └── Titanic.csv
│
├── Tests/
│   ├── breastCancer/
│   │   ├── ADAM/
│   │   │   ├── ADAM.ipynb
│   │   │   └── ADAM.py
│   │   ├── L_BFGS_B/
│   │   ├── SLSQP/
│   │   ├── AQGD/
│   │   ├── QNSPSA/
│   │   └── COBYLA/
│   ├── Diabetes/
│   │   └── [same structure as breastCancer]
│   └── Titanic/
│       └── [same structure as breastCancer]
│
├── Results/
│   ├── breastCancer/
│   ├── Diabetes/
│   └── Titanic/
│
└── sysPath/
    ├── breastCancer.py       # Dataset-specific preprocessing
    ├── summarize.py          # Evaluation, plotting, and reporting utilities
    └── ...
```

Each optimizer folder contains:
- `.ipynb` — Jupyter Notebook with documented tests and inline outputs.
- `.py` — Terminal-executable version (recommended for speed).

Each trained model saves:
- `{TestName}.model` — Serialized trained model.
- Confusion matrix figures.
- Classification report text file.
- `summary.xlsx` — Aggregated results across all 6 tests for that optimizer.

---

## Requirements

- Python 3.10+
- Qiskit 0.44+
- qiskit-machine-learning
- qiskit-algorithms
- scikit-learn
- imbalanced-learn (for SMOTE)
- pandas
- openpyxl
- matplotlib

---

## Installation

```bash
git clone https://github.com/your-username/Quantum-ML.git
cd Quantum-ML

pip install qiskit qiskit-machine-learning qiskit-algorithms
pip install scikit-learn imbalanced-learn pandas openpyxl matplotlib
```

---

## Usage

Each optimizer script is self-contained. To run the ADAM tests on the Breast Cancer dataset:

```bash
cd Tests/breastCancer/ADAM
python ADAM.py
```

The script will:
1. Load and preprocess the dataset.
2. Run all 6 feature map / ansatz combinations.
3. Save trained models to `ADAM/Trained Models/`.
4. Save confusion matrix figures and classification reports to `ADAM/Results/`.
5. Write a `summary.xlsx` with all metrics for quick comparison.

To run a different optimizer, navigate to its folder and execute the corresponding `.py` file.

---

## Citation

If you use this work, please cite:

```
Mohamed Aly, Manar Abu Talib, Salma Fadaaq, Qassim Nasir,
"Experimental Benchmarking of Quantum Machine Learning Classifiers" University of Sharjah, UAE.
```
