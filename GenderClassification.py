from sklearn import tree
from sklearn.metrics import accuracy_score

# [height , weight , shoe_size]
# list copied from the source 
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

Classifier = tree.DecisionTreeClassifier()

Classifier = Classifier.fit(X , Y)

prediction = Classifier.predict(X)

acc_dec = accuracy_score(Y,prediction)
print(acc_dec)

