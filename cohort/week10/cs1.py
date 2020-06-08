import numpy as np
from sklearn.metrics import confusion_matrix

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