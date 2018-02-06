from sklearn import tree

# [heignt, weight, shoe size]
X = [ [170,65,41], [168,65,39], [172,70,44], [140,60, 36] , [137,55, 34] , [165,60,38], [150,55,35], [170,55,40], [160,60,38], [150,60,36] ]

# ['Gender']
Y = ['male','female','male','female','male','female','male','female','male','male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

height = int(input("Height: "))
weight = int(input("Weight: "))
shoeSize = int(input("Shoe Size: "))
prediction = clf.predict([[height,weight,shoeSize]])
print(prediction)