from dataset import movie_dataset, movie_labels
from sklearn.neighbors import KNeighborsClassifier

true_false_list = []

# print(labels)

for i in range(100):
  i += 1
  classifier = KNeighborsClassifier(n_neighbors = i)
  classifier.fit(movie_dataset, labels)
  unknown_points = [
  [.45, .2, .5],
  [.25, .8, .9],
  [.1, .1, .9]
  ]
  unknown_labels = [0, 1, 2]
  y_predicted = classifier.predict(unknown_points)

  #Below I looked at the ways at the different possible ways one could yield 66%, 100%, or 33% or 0%. first elif function describes all the ways one could create 66% on the lists. Didn't use nested for loop for time complexity.  

  if unknown_labels[0] == y_predicted [0] and unknown_labels[1] == y_predicted[1] and unknown_labels[2] == y_predicted[2]:
    true_false_list.append([i, 3/3])
  elif (unknown_labels[0] == y_predicted[0] and unknown_labels[1] == y_predicted[1] and unknown_labels[2] != y_predicted[2]) or (unknown_labels[0] != y_predicted[0] and unknown_labels[1] == y_predicted[1] and unknown_labels[2] == y_predicted[2]) or(unknown_labels[0] == y_predicted[0] and unknown_labels[1] != y_predicted[1] and unknown_labels[2] == y_predicted[2]):
    true_false_list.append([i, 2/3])
  elif (unknown_labels[0] != y_predicted[0] and unknown_labels[1] != y_predicted[1] and unknown_labels[2] == y_predicted[2]) or (unknown_labels[0] == y_predicted[0] and unknown_labels[1] != y_predicted[1] and unknown_labels[2] != y_predicted[2]) or (unknown_labels[0] != y_predicted[0] and unknown_labels[1] == y_predicted[1] and unknown_labels[2] != y_predicted[2]):
    true_false_list.append([i, 1/3])
  else:
    true_false_list.append([i, 0])



true_false_list.sort()
print(true_false_list)




# classifier = KNeighborsClassifier(n_neighbors = 5)

# classifier.fit(movie_dataset, labels)

# unknown_points = [
#   [.45, .2, .5],
#   [.25, .8, .9],
#   [.1, .1, .9]
# ]

# print(classifier.predict(unknown_points))
