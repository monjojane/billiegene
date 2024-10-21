import pandas as pd

def undersample_data(info_file, output_file, minority_ratio=0.4):
    # Load the labels data
    try:
        labels = pd.read_csv(info_file)  # Load the labels from the provided CSV file path
        print(f"Loaded {len(labels)} rows from {info_file}.")
    except Exception as e:
        print(f"Error loading labels file: {e}")
        return

    # Check if the 'label' column exists
    if 'label' not in labels.columns:
        print("Error: 'label' column not found in the dataset.")
        return

    # Separate the majority (0) and minority (1) classes
    majority_class = labels[labels['label'] == 0]
    minority_class = labels[labels['label'] == 1]

    print(f"Majority class count: {len(majority_class)}")
    print(f"Minority class count: {len(minority_class)}")

    if len(minority_class) == 0:
        print("No minority class samples found.")
        return

    # Calculate the number of majority samples needed to achieve the desired ratio
    # Ratio of minority to majority should be 4:6
    num_minority = len(minority_class)
    num_majority = int((num_minority * (1 - minority_ratio)) / minority_ratio)  # Adjusting the majority class

    print(f"Number of majority samples to be selected: {num_majority}")

    # Ensure we do not sample more than available in the majority class
    if num_majority > len(majority_class):
        print("Not enough majority samples to achieve the desired ratio.")
        return

    # Undersample the majority class to match the calculated ratio
    majority_class_undersampled = majority_class.sample(n=num_majority, random_state=42)

    # Combine the undersampled majority class with the minority class
    balanced_labels = pd.concat([majority_class_undersampled, minority_class])

    # Shuffle the dataset
    balanced_labels = balanced_labels.sample(frac=1, random_state=42).reset_index(drop=True)

    # Save the new balanced dataset to a CSV file
    try:
        balanced_labels.to_csv(output_file, index=False)
        print(f"Balanced dataset saved to {output_file}.")
    except Exception as e:
        print(f"Error saving balanced dataset: {e}")

if __name__ == "__main__":
    info_file = "aggregated.csv"  # Path to your original labels file
    output_file = "balanced_labels.csv"  # Path to save the new balanced dataset
    undersample_data(info_file, output_file, minority_ratio=0.4)
