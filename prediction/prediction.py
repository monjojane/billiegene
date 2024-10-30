import pandas as pd
import joblib

with open('/Users/jheongry/Documents/GitHub/billiegene/model/rf_model_reduced_tuned_kfold.pkl', 'rb') as f: # path where trained model is saved
    model = joblib.load(f)

def parse_csv(csv_file):
    return pd.read_csv(csv_file)

# Function to make predictions
def predict_m6a_modifications(model, csv_file, output_csv):
    # Parsing the new data
    parsed_df = parse_csv(csv_file)

    # Preprocess the data (dropping unnecessary columns and converting to numeric)
    X_new = parsed_df.drop(columns=['transcript_id', 'transcript_position', 'nucleotide_sequence', 'dwelling_time_flank2'], errors='ignore')

    X_new = X_new.apply(pd.to_numeric, errors='coerce')
    X_new = X_new.dropna()

    # Predict probabilities (the `score` for m6A modification)
    y_proba = model.predict_proba(X_new)[:, 1]  # Get the probability for class 1 (m6A modification)

    # Create a DataFrame with 'transcript_id', 'transcript_position', and 'score'
    predictions_df = pd.DataFrame({
        'transcript_id': parsed_df['transcript_id'],
        'transcript_position': parsed_df['transcript_position'],
        'score': y_proba  # probability predicted by the model
    })

    # save predictions to a csv file with 17 decimal places for 'score'
    predictions_df.to_csv(output_csv, index=False, sep=',', float_format="%.17f")

    print(f"\nPredictions saved to {output_csv}")

csv_file = "/Users/jheongry/Documents/GitHub/billiegene/data/rf_aggregated2.csv"  # path to parsed and aggregated csv file 
output_csv = "/Users/jheongry/Documents/GitHub/billiegene/prediction/predicted_m6A_sites_dataset2.csv"  # path to the output csv file
predict_m6a_modifications(model, csv_file, output_csv)
