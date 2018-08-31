from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier

# [height , weight , shoe_size]
# list copied from the source 
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

Classifier1 = tree.DecisionTreeClassifier()

Classifier1 = Classifier1.fit(X , Y)

prediction = Classifier1.predict(X)

#accuracy for Decision Tree Classifier
acc = accuracy_score(Y,prediction)
print(acc)


Classifier2 = MLPClassifier()

Classifier2 = Classifier2.fit(X, Y)

prediction = Classifier2.predict(X)

#accuracy for MLP
acc = accuracy_score(Y,prediction)
print(acc)

Classifier3 = KNeighborsClassifier(n_neighbors=3)

Classifier3 = Classifier3.fit(X, Y)

prediction = Classifier3.predict(X)

#accuracy for KNN
acc = accuracy_score(Y,prediction)
print(acc)

Classifier4 = AdaBoostClassifier(tree.DecisionTreeClassifier(max_depth=1))

Classifier4 = Classifier4.fit(X, Y)

prediction = Classifier4.predict(X)

#accuracy for Adaboost
acc = accuracy_score(Y,prediction)
print(acc)







