#Loading the Dataset
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

data_loaded = load_breast_cancer()
X = data_loaded.data
y = data_loaded.target
#Splitting the dataset into training and testing variables

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=20)
 
#keeping 80% as training data and 20% as testing data.
 
#Calling the Class
naive_bayes = GaussianNB()
 
#Fitting the data to the classifier
naive_bayes.fit(X_train , y_train)
 
#Predict on test data
y_predicted = naive_bayes.predict(X_test)
print(y_predicted);

#Import metrics class from sklearn
 
accuracy = metrics.accuracy_score(y_predicted , y_test)
print(accuracy);