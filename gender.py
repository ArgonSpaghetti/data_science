from sklearn import tree


shoe_size_height_weight = [[181,80,44],[177,70,43],[160,60,38],
     [154,54,37],[166,65,40],[190,90,47],
     [175,64,38],[177,70,40],[159,55,37],
    [171,75,42],[181,85,43]]

gender = ["male","female","female","female",
     "male", "male", "male", "female","male", 
     "female", "male"]


clf = tree.DecisionTreeClassifier()

clf = clf.fit(shoe_size_height_weight, gender)

pred = clf.predict([[170, 70, 40]])
print(pred)
