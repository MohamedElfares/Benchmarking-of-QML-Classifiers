
## Test 1
### Configurations:
<pre>
  Ansatz used:          RealAmplitudes
  FeatureMap used:      ZFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       1242s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.52      0.37      0.43        43
           B       0.67      0.79      0.73        71

    accuracy                           0.63       114
   macro avg       0.60      0.58      0.58       114
weighted avg       0.61      0.63      0.62       114
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
  Execution Time:       632s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.78      0.65      0.71        43
           B       0.81      0.89      0.85        71

    accuracy                           0.80       114
   macro avg       0.79      0.77      0.78       114
weighted avg       0.80      0.80      0.79       114
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
  Execution Time:       651s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.77      0.63      0.69        43
           B       0.80      0.89      0.84        71

    accuracy                           0.79       114
   macro avg       0.78      0.76      0.77       114
weighted avg       0.79      0.79      0.78       114
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
  Execution Time:       2642s
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
  Execution Time:       2528s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.95      0.86      0.90        43
           B       0.92      0.97      0.95        71

    accuracy                           0.93       114
   macro avg       0.93      0.92      0.92       114
weighted avg       0.93      0.93      0.93       114
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
  Execution Time:       2061s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.95      0.86      0.90        43
           B       0.92      0.97      0.95        71

    accuracy                           0.93       114
   macro avg       0.93      0.92      0.92       114
weighted avg       0.93      0.93      0.93       114
</pre>

<img src='Results/Test 6.png' alt='Test 6.png' width=50% height=50%>

---

<br>
<br>

<img src='Performance.png' alt='Performance.png'>
