
## Test 1
### Configurations:
<pre>
  Ansatz used:          RealAmplitudes
  FeatureMap used:      ZFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       741s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.43      0.42      0.42        43
           B       0.65      0.66      0.66        71

    accuracy                           0.57       114
   macro avg       0.54      0.54      0.54       114
weighted avg       0.57      0.57      0.57       114
</pre>

<img src='Results/Test 1.png' alt='Test 1.png' width=50% height=50%>

---

<br>
<br>

## Test 2
### Configurations:
<pre>
  Ansatz used:          RealAmplitudes
  FeatureMap used:      ZZFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       1336s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.80      0.74      0.77        43
           B       0.85      0.89      0.87        71

    accuracy                           0.83       114
   macro avg       0.83      0.82      0.82       114
weighted avg       0.83      0.83      0.83       114
</pre>

<img src='Results/Test 2.png' alt='Test 2.png' width=50% height=50%>

---

<br>
<br>

## Test 3
### Configurations:
<pre>
  Ansatz used:          RealAmplitudes
  FeatureMap used:      PauliFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       1379s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.88      0.67      0.76        43
           B       0.83      0.94      0.88        71

    accuracy                           0.84       114
   macro avg       0.85      0.81      0.82       114
weighted avg       0.85      0.84      0.84       114
</pre>

<img src='Results/Test 3.png' alt='Test 3.png' width=50% height=50%>

---

<br>
<br>

## Test 4
### Configurations:
<pre>
  Ansatz used:          TwoLocal
  FeatureMap used:      ZFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       1111s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       1.00      0.79      0.88        43
           B       0.89      1.00      0.94        71

    accuracy                           0.92       114
   macro avg       0.94      0.90      0.91       114
weighted avg       0.93      0.92      0.92       114
</pre>

<img src='Results/Test 4.png' alt='Test 4.png' width=50% height=50%>

---

<br>
<br>

## Test 5
### Configurations:
<pre>
  Ansatz used:          TwoLocal
  FeatureMap used:      ZZFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       1694s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.97      0.79      0.87        43
           B       0.89      0.99      0.93        71

    accuracy                           0.91       114
   macro avg       0.93      0.89      0.90       114
weighted avg       0.92      0.91      0.91       114
</pre>

<img src='Results/Test 5.png' alt='Test 5.png' width=50% height=50%>

---

<br>
<br>

## Test 6
### Configurations:
<pre>
  Ansatz used:          TwoLocal
  FeatureMap used:      PauliFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       1697s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.97      0.84      0.90        43
           B       0.91      0.99      0.95        71

    accuracy                           0.93       114
   macro avg       0.94      0.91      0.92       114
weighted avg       0.93      0.93      0.93       114
</pre>

<img src='Results/Test 6.png' alt='Test 6.png' width=50% height=50%>

---

<br>
<br>

<img src='Performance.png' alt='Performance.png'>
