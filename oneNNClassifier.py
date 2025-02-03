import numpy as np

class oneNNClassifier():

    def __init__(self, data, labels, weights=None):
        self.data = data
        self.labels = labels
        self.weights = weights

    def predict(self, x_test, size, storage, weighted=False):
        storage[size] = []

        for x1 in x_test:
            target_class = -1
            minDist = np.inf

            for i in range(len(self.data)):
                x2 = self.data[i]

                # Calculate euclidean distance (L2)
                if weighted and self.weights is not None:
                    distance = np.linalg.norm(x1 - x2) / self.weights[i] # lesser the similarity larger the distance
                else:
                    distance = np.linalg.norm(x1 - x2)

                # Update target class if needed
                if distance < minDist:
                    minDist = distance
                    target_class = self.labels[i]

            storage[size].append(target_class)