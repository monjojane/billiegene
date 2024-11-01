#UNDERBALANCED tuned, feature dropped, kfold
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.preprocessing import LabelBinarizer
import pandas as pd
import numpy as np
import joblib

# Best hyperparameters from tuning
best_hyperparameters = {
    'n_estimators': 110,
    'max_depth': 20,
    'min_samples_split': 4,
    'min_samples_leaf': 3,
    'max_features': 'log2',
    'bootstrap': True
}

# Define Stratified K-Fold Cross-Validation
n_splits = 5
skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

# Initialize lists to store metrics for each fold
accuracy_list, precision_list, recall_list, f1_list, auc_roc_list = [], [], [], [], []
confusion_matrices = [] 

# Identify and remove the least important feature
importance_df = pd.DataFrame({
    'Feature': X_underbalanced.columns,
    'Importance': rf_model.feature_importances_
}).sort_values(by='Importance', ascending=False)

least_important_feature = importance_df.tail(1)['Feature'].values[0]
print(f"Removing least important feature: {least_important_feature}")

# Loop over each fold in Stratified K-Fold
for fold, (train_index, test_index) in enumerate(skf.split(X_underbalanced, y_underbalanced), 1):
    # Split the data into training and testing sets
    X_train, X_test = X_underbalanced.iloc[train_index], X_underbalanced.iloc[test_index]
    y_train, y_test = y_underbalanced.iloc[train_index], y_underbalanced.iloc[test_index]

    # Drop the least important feature from the datasets
    X_train_reduced = X_train.drop(columns=[least_important_feature])
    X_test_reduced = X_test.drop(columns=[least_important_feature])

    # Train Random Forest model with the best hyperparameters
    rf_model_reduced_tuned_kfold = RandomForestClassifier(**best_hyperparameters, random_state=42, n_jobs=-1)
    rf_model_reduced_tuned_kfold.fit(X_train_reduced, y_train)

    # Make predictions
    y_pred = rf_model_reduced_tuned_kfold.predict(X_test_reduced)
    y_pred_proba = rf_model_reduced_tuned_kfold.predict_proba(X_test_reduced)[:, 1]  # Probabilities for class 1

    # Ensure predictions and test labels are integers
    y_test = y_test.astype(int)
    y_pred = y_pred.astype(int)

    # Calculate evaluation metrics for the current fold
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='binary', zero_division=0)
    recall = recall_score(y_test, y_pred, average='binary', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='binary', zero_division=0)

    # Binarize the labels for ROC AUC calculation
    lb = LabelBinarizer()
    y_test_binarized = lb.fit_transform(y_test)
    auc_roc = roc_auc_score(y_test_binarized, y_pred_proba)

    # Confusion matrix for the current fold
    cm = confusion_matrix(y_test, y_pred)
    confusion_matrices.append(cm)

    # Append metrics for the current fold
    accuracy_list.append(accuracy)
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)
    auc_roc_list.append(auc_roc)

    # Print metrics for the current fold
    print(f"Fold {fold} results:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"AUC-ROC: {auc_roc:.4f}")
    print(f"Confusion Matrix:\n{cm}\n")

# Compute average metrics across all folds
print(f"Average Accuracy: {np.mean(accuracy_list):.4f}")
print(f"Average Precision: {np.mean(precision_list):.4f}")
print(f"Average Recall: {np.mean(recall_list):.4f}")
print(f"Average F1 Score: {np.mean(f1_list):.4f}")
print(f"Average AUC-ROC: {np.mean(auc_roc_list):.4f}")

# Print the confusion matrices for each fold
for i, cm in enumerate(confusion_matrices, 1):
    print(f"Confusion Matrix for Fold {i}:\n{cm}\n")

# Save the final model
joblib.dump(rf_model_reduced_tuned_kfold, '../models/model.pkl') # path to save trained model to
print("Final model saved as 'model.pkl'")
