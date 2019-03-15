# class8


 docker build -t allys/hw8:v1 ./


Basic 2: Refactor plotting code to work with sklearn.datasets
         run docker 
	 docker run -it --entrypoint '/bin/sh' allys/hw8:v1
         run the python script
         'python3 wine.py'

          Only 200 graphs will be printed and then it will exit.
	  There will be a message to that effect.







Basic 3: perform classification
         build docker container
         'docker build -t allys/hw8:v1 ./'
          Run docker container
	  'docker run -ti allys/hw8:v1'


* * * * * * *   K-NEAREST NEIGHBOUR   * * * * * * * * *


confusion_matrix
[[13  1  0]
 [ 1 12  3]
 [ 1  2  3]]

classificatio_report
              precision    recall  f1-score   support

           0       0.87      0.93      0.90        14
           1       0.80      0.75      0.77        16
           2       0.50      0.50      0.50         6

   micro avg       0.78      0.78      0.78        36
   macro avg       0.72      0.73      0.72        36
weighted avg       0.78      0.78      0.78        36


f1_score
0.7235817575083426


performance of estimator
0.7777777777777778



* * * * * * *   Gaussian   * * * * * * * * *


confusion_matrix
[[14  0  0]
 [ 2 13  1]
 [ 0  0  6]]

classificatio_report
              precision    recall  f1-score   support

           0       0.88      1.00      0.93        14
           1       1.00      0.81      0.90        16
           2       0.86      1.00      0.92         6

   micro avg       0.92      0.92      0.92        36
   macro avg       0.91      0.94      0.92        36
weighted avg       0.93      0.92      0.92        36


f1_score
0.9176539935160625


performance of estimator


0.9166666666666666

* * * * * * *   Decision Tree   * * * * * * * * *


confusion_matrix
[[14  0  0]
 [ 5  9  2]
 [ 0  0  6]]

classificatio_report
              precision    recall  f1-score   support

           0       0.74      1.00      0.85        14
           1       1.00      0.56      0.72        16
           2       0.75      1.00      0.86         6

   micro avg       0.81      0.81      0.81        36
   macro avg       0.83      0.85      0.81        36
weighted avg       0.86      0.81      0.79        36


f1_score
0.8085425685425686


performance of estimator
0.8055555555555556



* * * * * * *   Stochastic Gradient Descent   * * * * * * *


confusion_matrix
[[11  3  0]
 [ 0 16  0]
 [ 1  5  0]]

classificatio_report
              precision    recall  f1-score   support

           0       0.92      0.79      0.85        14
           1       0.67      1.00      0.80        16
           2       0.00      0.00      0.00         6

   micro avg       0.75      0.75      0.75        36
   macro avg       0.53      0.60      0.55        36
weighted avg       0.65      0.75      0.68        36


f1_score
0.5487179487179487


performance of estimator
0.75



* * * * * * * * * * * ** * * *
*                            *
*        THE END             *
*                            *
* * * * * * * * ** * * * * * *

