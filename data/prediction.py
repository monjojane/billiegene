import pandas as pd
from tensorflow.keras.models import load_model  # Use Keras to load the neural network model
import joblib
import numpy as np

# Load your trained model
model = load_model('m6A_model.h5')  # Replace with the actual path to your saved model

# Define a function to parse and load the CSV data
def parse_csv(csv_file):
    # Load the CSV data into a DataFrame
    return pd.read_csv(csv_file)

# Define a function to make predictions
def predict_m6a_modifications(model, csv_file, output_csv):
    # Parse the new data
    parsed_df = parse_csv(csv_file)
    
    # Check the columns of the parsed data to ensure correctness
    print("Columns in the loaded data:", parsed_df.columns)

    # Preprocess the data (dropping unnecessary columns and converting to numeric)
    if all(col in parsed_df.columns for col in ['Transcript_ID', 'Position', 'Sequence']):
        X_new = parsed_df.drop(columns=['Transcript_ID', 'Position', 'Sequence'])
        X_new = X_new.apply(pd.to_numeric, errors='coerce')
        X_new = X_new.dropna()

        scaler = joblib.load('scaler.pkl')  # Load your scaler
        X_new = scaler.transform(X_new)  # Scale the new data

        # Predict probabilities (the `score` for m6A modification)
        y_proba = model.predict(X_new).flatten()  # Flatten the array to ensure it's 1D

        # Create a DataFrame with 'transcript_id', 'transcript_position', and 'score'
        predictions_df = pd.DataFrame({
            'transcript_id': parsed_df['Transcript_ID'],
            'transcript_position': parsed_df['Position'],
            'score': y_proba  # This is the probability predicted by the model
        })

        # Save the predictions to a CSV file
        predictions_df.to_csv(output_csv, index=False, sep=',')
        print(f"Predictions saved to {output_csv}")
    else:
        print("Error: Required columns not found in the dataset!")

# Example of using the function
csv_file = "aggregated2_new.csv"  # Replace with the path to your input CSV file
output_csv = "billiegene_dataset2_2.csv"  # Name of the output CSV file
predict_m6a_modifications(model, csv_file, output_csv)
