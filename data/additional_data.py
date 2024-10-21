import pandas as pd
from imblearn.over_sampling import RandomOverSampler

def oversample_minority(info_file, output_file):
    # Load the original dataset
    try:
        labels = pd.read_csv(info_file)
        print(f"Loaded {len(labels)} rows from {info_file}.")
    except Exception as e:
        print(f"Error loading labels file: {e}")
        return

    # Check if 'label' column exists
    if 'label' not in labels.columns:
        print("Error: 'label' column not found in the dataset.")
        return

    # Separate features (X) and target (y)
    X = labels.drop(columns=['label'])  # Assuming all other columns are features
    y = labels['label']

    # Count the number of samples for each class
    majority_class_count = y.value_counts()[0]  # Count of label 0 (majority)
    minority_class_count = y.value_counts()[1]  # Count of label 1 (minority)

    print(f"Majority class count (label 0): {majority_class_count}")
    print(f"Minority class count (label 1): {minority_class_count}")

    # Desired number of samples for the minority class to maintain a 4:6 ratio
    target_minority_count = int(majority_class_count * (4 / 6))

    # Initialize the RandomOverSampler with the desired target ratio
    oversampler = RandomOverSampler(sampling_strategy={1: target_minority_count}, random_state=42)

    # Fit and resample the data
    X_resampled, y_resampled = oversampler.fit_resample(X, y)

    # Combine the resampled features and target into a new DataFrame
    balanced_data = pd.concat([X_resampled, y_resampled], axis=1)

    # Save the balanced dataset to a CSV file
    try:
        balanced_data.to_csv(output_file, index=False)
        print(f"Balanced dataset saved to {output_file}.")
    except Exception as e:
        print(f"Error saving balanced dataset: {e}")

if __name__ == "__main__":
    info_file = "aggregated.csv"  # Path to your original labels file
    output_file = "overbalanced_labels.csv"  # Path to save the new balanced dataset
    oversample_minority(info_file, output_file)