import numpy as np
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

def get_metrics(actual_targets, predicted_targets, labels):

    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)

    correct = 0
    for i in range(len(c_matrix)):
        correct += c_matrix[i][i]

    accuracy = round(correct / max(len(actual_targets), len(predicted_targets)), 3)

    sensitivity = round(c_matrix[1][1] / sum(c_matrix[1]), 3)

    false_positive = round(c_matrix[0][1] / sum(c_matrix[0]), 3)

    output = {'confusion matrix': c_matrix, 'total records': max(len(actual_targets), len(predicted_targets)), 'accuracy': accuracy, 'sensitivity': sensitivity, 'false positive rate': false_positive}

    return output

def normalize_minmax(data):
    if len(data.shape) != 2:
        return None

    for i in range(len(data[0])):
        maximum = np.max(data[:, i])
        minimum = np.min(data[:, i])
        data[:, i] = (data[:, i] - minimum) / (maximum - minimum)

    return data

def knn_classifier_full(bunchobject, feature_list, size, seed):
    data = bunchobject.data[:, feature_list]
    data = normalize_minmax(data)
    target = bunchobject.target
    data_train, data_part2, target_train, target_part2 = train_test_split(data, target, test_size=size, random_state=seed)
    data_valid, data_test, target_valid, target_test = train_test_split(data_part2, target_part2, test_size=0.5, random_state=seed)
    acc = []
    metrics = []

    for k in range(1, 21):
        clf = neighbors.KNeighborsClassifier(n_neighbors=k)
        clf.fit(data_train, target_train)
        target_predicted = clf.predict(data_valid)
        results = get_metrics(target_valid, target_predicted, [1, 0])
        accuracy = results.get('accuracy')
        acc.append(accuracy)
        metrics.append((target_valid, target_predicted))

    max_acc = max(acc)
    best_k = acc.index(max_acc) + 1
    clf = neighbors.KNeighborsClassifier(n_neighbors=best_k)
    clf.fit(data_train, target_train)
    target_predicted = clf.predict(data_test)
    out_results = {'best k': best_k, 'validation set': get_metrics(metrics[best_k - 1][0], metrics[best_k - 1][1], [1, 0]), 'test set': get_metrics(target_test, target_predicted, [1, 0])}
    return out_results