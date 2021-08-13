from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve,auc
from scikitplot.metrics import plot_roc
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

data = pd.read_csv("A+B=C.csv")
print(data.shape)

data = data.replace(to_replace="?",value=np.nan)
data = data.dropna(how='any')
print(data.shape)

data_label = ['HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'Resp', 'Age', 'Gender', 'HospAdmTime', 'ICULOS', 'SepsisLabel']
X_train, X_test, y_train, y_test = train_test_split(data[data_label[:10]],data[data_label[10]],test_size=0.3, random_state=2021)

print(X_train.shape,X_test.shape)
print(y_train.shape,y_test.shape)

from imblearn.under_sampling import RandomUnderSampler
# instantiating the random undersampler
rus = RandomUnderSampler()
# resampling X, y
X_rus, y_rus = rus.fit_resample(X_train, y_train)# new class distribution
print(X_rus.shape, y_rus.shape )

# KNN
print("KNN:")
knn = KNeighborsClassifier()
knn.fit(X_rus, y_rus)
preproKnn = knn.predict(X_test)
print('KNN classification_report: \n', classification_report(preproKnn, y_test))
fpr, tpr, thresholds = roc_curve(y_test, preproKnn, pos_label=1)
print('AUC',auc(fpr, tpr))
plot_roc(y_test, knn.predict_proba(X_test))
# plt.show()

print("------------------------------------------------------")

from sklearn import tree

Tree = tree.DecisionTreeClassifier()
Tree.fit(X_rus, y_rus)
preproTree = Tree.predict(X_test)
print('Tree classification_report: \n', classification_report(preproTree, y_test))
fpr, tpr, thresholds = roc_curve(y_test, preproTree, pos_label=1)
print('AUC',auc(fpr, tpr))
plot_roc(y_test, Tree.predict_proba(X_test))

# plt.show()
print("------------------------------------------------------")

print("SVM:")

from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

SVM = SVC(kernel='rbf', probability=True,C=10)
# SVM = Pipeline(( ("scaler", StandardScaler()),
#                      ("linear_svc", LinearSVC(C=100, loss="hinge",max_iter=10000)) ,))
SVM.fit(X_rus, y_rus)
preproSVM = SVM.predict(X_test)
print('SVM classification_report: \n', classification_report(preproSVM, y_test))
fpr, tpr, thresholds = roc_curve(y_test, preproSVM, pos_label=1)
print('AUC',auc(fpr, tpr))
plot_roc(y_test, SVM.predict_proba(X_test))
plt.show()
# print("------------------------------------------------------")
