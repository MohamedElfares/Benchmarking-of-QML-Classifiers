
## Test 1
### Configurations:
<pre>
  ansatz used:          RealAmplitudes
  featureMap used:      ZFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       738s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.52      0.35      0.42        43
           B       0.67      0.80      0.73        71

    accuracy                           0.63       114
   macro avg       0.59      0.58      0.57       114
weighted avg       0.61      0.63      0.61       114
</pre>

<img src='Results/Test 1.png' alt='Test 1.png' width=50% height=50%>

---

<br>
<br>

## Test 2
### Configurations:
<pre>
  ansatz used:          RealAmplitudes
  featureMap used:      ZZFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       904s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.79      0.70      0.74        43
           B       0.83      0.89      0.86        71

    accuracy                           0.82       114
   macro avg       0.81      0.79      0.80       114
weighted avg       0.81      0.82      0.81       114
</pre>

<img src='Results/Test 2.png' alt='Test 2.png' width=50% height=50%>

---

<br>
<br>

## Test 3
### Configurations:
<pre>
  ansatz used:          RealAmplitudes
  featureMap used:      PauliFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       655s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       0.79      0.70      0.74        43
           B       0.83      0.89      0.86        71

    accuracy                           0.82       114
   macro avg       0.81      0.79      0.80       114
weighted avg       0.81      0.82      0.81       114
</pre>

<img src='Results/Test 3.png' alt='Test 3.png' width=50% height=50%>

---

<br>
<br>

## Test 4
### Configurations:
<pre>
  ansatz used:          TwoLocal
  featureMap used:      ZFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       5375s
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
  ansatz used:          TwoLocal
  featureMap used:      ZZFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       2323s
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
  ansatz used:          TwoLocal
  featureMap used:      PauliFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       1818s
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
