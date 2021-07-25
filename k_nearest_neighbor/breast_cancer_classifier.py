import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
breast_cancer_data = load_breast_cancer()

print(breast_cancer_data.data[0])
print(breast_cancer_data.target[0])
print(breast_cancer_data.target_names[0])

training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 12)

print(training_data.shape)
print(training_labels.shape)

accuracy_list_with_k = []
k_list = []
accuracies = []
for i in range(1, 100):
  k_list.append(i)
  classifier = KNeighborsClassifier(n_neighbors = i)

  classifier.fit(training_data, training_labels)

  score = classifier.score(validation_data, validation_labels)

  accuracy_list_with_k.append([score, i])
  accuracies.append(score)

accuracy_list_with_k.sort()

plt.plot(k_list, accuracies)
plt.xlabel("Validation Accuracy")
plt.ylabel("Breast Cancer accuracy")
plt.show()
