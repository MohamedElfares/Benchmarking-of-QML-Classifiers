
## Test 1
### Configurations:
<pre>
  FeatureMap used:      ZFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       635s
</pre>

<br>
<br>

### Results Summary:
<pre>
              precision    recall  f1-score   support

           M       1.00      0.81      0.90        43
           B       0.90      1.00      0.95        71

    accuracy                           0.93       114
   macro avg       0.95      0.91      0.92       114
weighted avg       0.94      0.93      0.93       114
</pre>

<img src='Results/Test 1.png' alt='Test 1.png' width=50% height=50%>

---

<br>
<br>

## Test 2
### Configurations:
<pre>
  FeatureMap used:      ZZFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       1626s
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

<img src='Results/Test 2.png' alt='Test 2.png' width=50% height=50%>

---

<br>
<br>

## Test 3
### Configurations:
<pre>
  FeatureMap used:      PauliFeatureMap
  # Qubits used:        2
  Ratio:                0.63:0.37
  SMOTE:                True
  Execution Time:       1603s
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

<img src='Results/Test 3.png' alt='Test 3.png' width=50% height=50%>

---

<br>
<br>

<img src='Performance.png' alt='Performance.png'>
