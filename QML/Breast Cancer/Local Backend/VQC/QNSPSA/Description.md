
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

           M       0.40      0.37      0.39        43
           B       0.64      0.66      0.65        71

    accuracy                           0.55       114
   macro avg       0.52      0.52      0.52       114
weighted avg       0.55      0.55      0.55       114
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
  Execution Time:       1327s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.89      0.72      0.79        43
           B       0.85      0.94      0.89        71

    accuracy                           0.86       114
   macro avg       0.87      0.83      0.84       114
weighted avg       0.86      0.86      0.86       114
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
  Execution Time:       1317s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.84      0.72      0.77        43
           B       0.84      0.92      0.88        71

    accuracy                           0.84       114
   macro avg       0.84      0.82      0.83       114
weighted avg       0.84      0.84      0.84       114
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
  Execution Time:       1110s
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
  Execution Time:       1685s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.94      0.79      0.86        43
           B       0.88      0.97      0.93        71

    accuracy                           0.90       114
   macro avg       0.91      0.88      0.89       114
weighted avg       0.91      0.90      0.90       114
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
  Execution Time:       1673s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       1.00      0.74      0.85        43
           B       0.87      1.00      0.93        71

    accuracy                           0.90       114
   macro avg       0.93      0.87      0.89       114
weighted avg       0.92      0.90      0.90       114
</pre>

<img src='Results/Test 6.png' alt='Test 6.png' width=50% height=50%>

---

<br>
<br>

<img src='Performance.png' alt='Performance.png'>
