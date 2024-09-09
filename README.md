<div style="text-align: justify">

# Model Structure
---

<br>

### Dimensionality Reduction
Dimensionality reduction involves converting data from a high-dimensional space to a low-dimensional space, aiming to preserve meaningful properties of the original data as closely as possible to its intrinsic dimension. In this context, I have opted for the `PCA` to perform the dimensionality reduction process.

<br>

### Data Normalization
Data normalization involves restructuring the data to eliminate any unstructured or redundant information, leading to a more efficient and logical way of storing the data. The primary objective of data normalization is to achieve a standardized data format throughout the entire system. For this purpose, I have selected the `StandardScaler` to execute the normalization process.

<br>

### Data Scaling
Data scaling is a process of transforming the data to fit within a specific scale, such as *[0, 100]* or *[0, 1]*. It is commonly used when applying methods that rely on measuring the distances between data points, such as Support Vector Machines (SVM) or k-Nearest Neighbors (KNN). To achieve this scaling, I have selected the `MinMaxScaler` as the chosen method to perform the scaling process.

<br>

### Feature Map
As the data is classical and represented by a set of bits, we require a method to encode this data into qubits. This step is crucial to achieve an effective quantum model. The process of converting classical data to qubits is commonly known as data encoding, data embedding, or data loading, and it is facilitated by the feature map. Recognizing the significance of this approach, I have decided to train our models using various feature maps, such as `PauliFeatureMap`, `ZZFeatureMap`, and `ZFeatureMap`. Each of these feature maps offers unique characteristics that can enhance the performance of our quantum models.

<br>

### Parameterized Quantum Circuit
The parameterized quantum circuit bears a resemblance to the layers found in classical neural networks. It consists of a collection of tunable parameters or weights. These weights are optimized to minimize an objective function that quantifies the disparity between predictions and known labeled data. To achieve this optimization, I intend to employ `RealAmplitudes` and `TwoLocal` methods. These approaches provide powerful capabilities to fine-tune the circuit's parameters, ultimately improving the overall performance of our quantum model.

<br>

### Data Optimization
Afterward, I proceed to select an optimization algorithm for the training process, aiming to expedite the training by utilizing a gradient-free optimizer. In this context, I have opted for a variety of data optimizers, including `ADAM`, `L-BFGS-B`, `SLSQP`, `AQGD`, `QNSPSA`, and `COBYLA`. Each of these optimizers provides different approaches to fine-tune the parameters efficiently, enhancing the overall training performance.

<br>

### Sampling
Moving on to the subsequent step, I determine the platform for training our classifier. The training process can be conducted either on a simulator or a real quantum computer. In this case, I will employ a simulators like `Sampler` and `Estimator`. If time permits, I may also explore the basis versions of earlier samplers for comparison and evaluation.

<br>

### Training Algorithm Selection and Fitting
During this stage, I will carefully choose the training algorithm from a selection of options, including `PegasosQSVC`, `QSVC`, `NeuralNetworkClassifier`, and `VQC`. The chosen algorithms `VQC` and `NeuralNetworkClassifier` will be utilized to train our model on the given dataset, allowing us to proceed with the training process.

<br>

### Running the Model
Finally, execute the trained model and patiently await the results. I also engage in the evaluation process by experimenting with parameters that directly influence the success ratio. These parameters include data preprocessing, the FeatureMap selection, data parametrization, and other relevant factors. Through careful experimentation, I aim to optimize the model's performance and achieve the best possible outcomes.

<br>
<br>
<br>

# Accuracy and Training Time
---
In this section, I will elucidate the factors that impact both accuracy and training time based on the observations and results obtained from various tests.

<br>

### Accuracy
I have noticed that the accuracy is affected by various factors some of them have strong impact on it and others has lite impace.

**Classifier**: Although the results from `VQC`, `NeuralNetworkClassifier`, `QSVC`, and `PegasosQSVC` classifiers were very close and similar, certain factors, such as FeatureMap and Anstaz, significantly influenced the accuracy.

**Optimizer**: The choice of optimizer plays a crucial role in determining accuracy. After analyzing six different optimizers mentioned in the *Data Optimization* section, I observed that `ADAM`, `L_BFGS_B`, and `SLSQP` are the recommended ones. These optimizers consistently maintained high accuracy levels, staying within a close range. However, it's worth noting that when combined with varying FeatureMap and Anstaz settings, some tests produced abnormal results compared to others. This behavior is closely linked to the data preprocessing, which I will elaborate on later.

**FeatureMap**: The impact of FeatureMap on accuracy is not substantial, but it is worth noting that `ZFeatureMap`, being the simplest among the three selected FeatureMaps, consistently achieves higher accuracy compared to `ZZFeatureMap` and `PauliFeatureMap` in the majority of tests. Moreover, in the specific tests involving additional experimental setups, `ZFeatureMap` is the preferred choice. Nevertheless, it's essential to acknowledge that `ZZFeatureMap` and `PauliFeatureMap` are also capable of achieving high accuracy and maintaining a close range. However, due to their increased complexity, they sometimes lead to longer training times.

**Data Preprocessing**: The data preprocessing stage holds utmost significance in both classical and quantum AI modeling. Properly preprocessed data guarantees high accuracy, regardless of other factors, while also ensuring consistent results. However, I encountered a particular challenge known as *Intertwined*, where certain features have duplicated values for different classes. This intertwining of data hinders the ability to discern boundaries between different classes, as evident in the *Diabetes* and *Titanic* datasets. To address this issue, I experimented with various data preprocessing techniques available on *Kaggle*, but the results remained largely unchanged. As a consequence, some tests exhibited abnormal outcomes due to this underlying problem. (Please note that an image titled `{output}` is available for each dataset in the VQC folder).

<br>

### Training Time
It should be noted that the training time is no less important than the accuracy, and therefore it had a share of interest in its results in every examination and stage of testing the variables, and it has special variables and others that are common with accuracy.

**Optimizer**: During the tests and analysis, it became evident that the choice of optimizer significantly influences the training time. Certain optimizers, such as *ADAM* and *QNSPSA*, may extend the model training duration to more than 8 hours, while others like *AQGD* might take one to two hours. In contrast, faster optimizers like *L_BFGS_B*, *SLSQP*, and *COBYLA* complete training within just a few minutes.

Moreover, it is crucial to highlight that each optimizer exhibits unique behavior when interacting with other factors, such as FeatureMap and ansatz, leading to distinct outcomes and potentially abnormal results.

**FeatureMap** and **Ansatz**: As previously stated, the chosen *ZFeatureMap* stands out as the simplest among the three FeatureMaps used in the tests. This simplicity has a noticeable impact on the training time. On the other hand, the *TwoLocal* ansatz is one of the factors that consistently resulted in abnormal outcomes across various optimizers.

However, what sets the *ZFeatureMap* apart is its resilience to the influence of the ansatz, regardless of its nature. In other words, the *ZFeatureMap* demonstrated a relatively stable performance, less affected by the choice of ansatz when compared to the other FeatureMaps.

**Dimension Reduction Level**: The level of dimension reduction is expected to significantly impact both accuracy and training time, but its effect is particularly notable in training time. In all the tests I conducted, I set the `PCA` (Principal Component Analysis) to reduce the data's dimension and complexity to *2*. However, in certain specialized tests, I increased the dimension reduction level to *5*.

Notably, when the model is trained with a dimension reduction level of *5*, the required training time is found to be approximately 1.5 to 2 times longer and in some cases, it even doubles compared to when the model is trained with a dimension reduction level of *2*. This illustrates the trade-off between achieving higher accuracy through dimensionality reduction and the associated increase in training time.

**maxiter**: The `maxiter` parameter is a crucial setting in optimizers, determining the maximum number of iterations performed on the data during the optimization process. Different optimizers have varying default values for this parameter; for instance, the `L_BFGS_B` optimizer typically has a default value of 15000, while the `SLSQP` optimizer's default value is set to 100.

Modifying the `maxiter` value, either increasing or decreasing it, slightly impacts the training time. For instance, raising the value may lead to more iterations and slightly extend the training time, while lowering it might result in fewer iterations and a marginal reduction in training time. The choice of `maxiter` should be made carefully, considering the trade-off between computational resources and convergence speed.

<br>
<br>
<br>

# Tests & Results
---
For each classifier, I have organized my work into two distinct main folders.

### Tests
In this directory, you will come across three main folders, each dedicated to a specific dataset: "**breastCancer**," "**Diabetes**," and "**Titanic**". Within these folders, you will find six versions, corresponding to the six optimizers previously mentioned and discussed. 

For each optimizer, I created a version in the form of a *.ipynb* file, where I meticulously documented all the tests conducted with that particular optimizer. Each optimizer version encompasses six distinct tests, based on different combinations of FeatureMap and Ansatz, resulting in a total of six tests for each optimizer.

Additionally, there is another version for each optimizer, saved with a *.py* extension, intended to be executed through the terminal. I believe executing the code this way is faster than using Jupyter Notebook.

In summary, I performed `36` tests for each dataset, culminating in more than `100` tests for the entire set of datasets.

<br>
<br>

### Results
The result directory is primarily designed for conducting additional tests on the optimal combinations of Optimizer, FeatureMap, and Ansatz that yield the highest accuracy while minimizing the training time. To determine the models to be further tested, a straightforward criterion is applied: the accuracy must be `0.7` or higher, and the training time should not exceed `30` minutes.

There are three main subfolders for each dataset, each containing a folder named after the selected version chosen for testing. Within these version folders, there may be subfolders representing different numbers of tests. In each test-numbered folder, you will find images displaying the confusion matrices generated from the additional tests, along with a file named `Description`, containing records for each test.

The additional tests can be divided into three parts:

First part [Test 0]: Multiple tests were conducted to explore the effects of enabling or disabling data normalization, performed using `StandardScaler`, and data scaling, conducted using `MinMaxScaler`, to achieve the best performance in terms of accuracy. Subsequently, the `maxiter` optimizer attribute was set to its default, and the model was trained using the entire dataset, with results recorded.

Second part [Test 1 - 5]: Using the same combinations of data normalization and scaling as before, the influence of different entanglement types in the ansatz was studied. These entanglement types included full, linear, reverse_linear, circular, and csa. The results were documented accordingly.

Third part [Test X+, X++]: From the previous tests, the highest accuracy with the least training time was selected. In [Test X+], the dimension reduction was changed from 2 to 5 to examine the effect of increasing the data depth on accuracy and training time. Meanwhile, in [Test X++], additional variations in data preprocessing were explored for some cases.

</div>
