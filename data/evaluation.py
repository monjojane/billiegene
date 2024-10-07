import numpy as np
import pandas as pd
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             confusion_matrix, roc_auc_score, roc_curve, auc, 
                             precision_recall_curve, matthews_corrcoef)
import matplotlib.pyplot as plt
import seaborn as sns

# Example function to evaluate a classification model
def evaluate_model(y_true, y_pred, y_pred_prob=None):
    # 1. Accuracy
    accuracy = accuracy_score(y_true, y_pred)
    
    # 2. Precision
    precision = precision_score(y_true, y_pred)
    
    # 3. Recall
    recall = recall_score(y_true, y_pred)
    
    # 4. F1 Score
    f1 = f1_score(y_true, y_pred)
    
    # 5. Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)
    
    # 6. AUC-ROC Score
    roc_auc = None
    if y_pred_prob is not None:
        roc_auc = roc_auc_score(y_true, y_pred_prob)
    
    # 7. Matthews Correlation Coefficient
    mcc = matthews_corrcoef(y_true, y_pred)
    
    # Print the metrics
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"Matthews Correlation Coefficient: {mcc:.4f}")
    if roc_auc is not None:
        print(f"AUC-ROC: {roc_auc:.4f}")
    
    # Display Confusion Matrix
    display_confusion_matrix(cm)
    
    # Plot AUC-ROC Curve
    if y_pred_prob is not None:
        plot_roc_curve(y_true, y_pred_prob)
    
    # Plot Precision-Recall Curve
    if y_pred_prob is not None:
        plot_precision_recall_curve(y_true, y_pred_prob)
    

def display_confusion_matrix(cm):
    # Plot Confusion Matrix using Seaborn
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.ylabel('Actual Label')
    plt.xlabel('Predicted Label')
    plt.title('Confusion Matrix')
    plt.show()


def plot_roc_curve(y_true, y_pred_prob):
    fpr, tpr, _ = roc_curve(y_true, y_pred_prob)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(6, 4))
    plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC Curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()


def plot_precision_recall_curve(y_true, y_pred_prob):
    precision, recall, _ = precision_recall_curve(y_true, y_pred_prob)
    plt.figure(figsize=(6, 4))
    plt.plot(recall, precision, color='green', lw=2)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.show()


# Example usage with some dummy data:
if __name__ == "__main__":
    # Assuming you have true labels (y_true) and predictions (y_pred) and prediction probabilities (y_pred_prob)
    
    # Replace this with actual labels and model predictions
    y_true = np.random.randint(0, 2, 100)  # True labels
    y_pred = np.random.randint(0, 2, 100)  # Predicted labels
    y_pred_prob = np.random.rand(100)  # Predicted probabilities for the positive class
    
    # Evaluate the model
    evaluate_model(y_true, y_pred, y_pred_prob)
