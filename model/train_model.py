import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (confusion_matrix, accuracy_score, precision_score,
                             recall_score, f1_score, roc_auc_score)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import shutil
from imblearn.under_sampling import RandomUnderSampler
import joblib

# Clear the previous tuner results
shutil.rmtree('keras_tuner/m6A_tuning_v2', ignore_errors=True)

# Load your data
df = pd.read_csv('../data/aggregated_new.csv')

# Preprocess the data
X = df[['Dwelling_time1', 'Std_dev_signal1', 'Mean_signal1', 
         'Dwelling_time2', 'Std_dev_signal2', 'Mean_signal2', 
         'Dwelling_time3', 'Std_dev_signal3', 'Mean_signal3',
         'Sum_Dwelling_Time', 'Abs_SD1_SD2', 'Abs_SD1_SD3', 
         'Abs_SD2_SD3', 'dwelling_time_2_IQ']]
y = df['label']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Calculate the desired counts for undersampling
count_1 = (y == 1).sum()  # Count of class '1'
desired_count_1 = count_1  # Keep all instances of class '1'
desired_count_0 = int(desired_count_1 * 4)  # 4 times the number of class '1'

# Set the sampling strategy for undersampling
sampling_strategy = {0: desired_count_0, 1: desired_count_1}

# Undersample to achieve the desired ratio
rus = RandomUnderSampler(sampling_strategy=sampling_strategy, random_state=42)
X_resampled, y_resampled = rus.fit_resample(X_scaled, y)

# Define the final model with the best hyperparameters
def create_model():
    model = Sequential()
    model.add(Dense(128, activation='relu', input_shape=(X_resampled.shape[1],)) )  # units_1
    model.add(Dropout(0.2))  # dropout
    model.add(Dense(16, activation='relu'))  # units_2
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer=Adam(learning_rate=0.0027098),  # learning_rate
                  loss='binary_crossentropy',
                  metrics=['AUC'])  # Track AUC during training
    return model

# Initialize the model
model = create_model()

# Train the model with the entire resampled dataset
model.fit(X_resampled, y_resampled, 
          epochs=30,
          batch_size=32,
          verbose=1)
# Save the model and scaler
model.save('m6A_model.h5')
joblib.dump(scaler, 'scaler.pkl')

# Final evaluation on the entire dataset
y_pred_prob = model.predict(X_resampled).flatten()
y_pred = (y_pred_prob > 0.5).astype(int)

# Calculate metrics
conf_matrix = confusion_matrix(y_resampled, y_pred)
accuracy = accuracy_score(y_resampled, y_pred)
precision = precision_score(y_resampled, y_pred)
recall = recall_score(y_resampled, y_pred)
f1 = f1_score(y_resampled, y_pred)
roc_auc = roc_auc_score(y_resampled, y_pred_prob)
loss_value = model.evaluate(X_resampled, y_resampled, verbose=0)[0]

# Print metrics and results
print("Confusion Matrix:\n", conf_matrix)
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("AUC-ROC:", roc_auc)
print("Loss Value of Best Model:", loss_value)
