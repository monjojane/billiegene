import json
import pandas as pd

def parse_data(json_file):
    # Initialize an empty list to hold the parsed data
    parsed_data = []

    # Open the file and read line by line
    with open(json_file, 'r') as f:
        for line in f:
            if line.strip():  # Skip empty lines
                try:
                    # Load the JSON data from the current line
                    json_data = json.loads(line)

                    # Iterate through the transcripts
                    for transcript_id, positions in json_data.items():
                        # Iterate through each position in the transcript
                        for pos, nucleotides in positions.items():
                            # Convert position to integer
                            pos = int(pos)
                            
                            # Iterate through the nucleotide combinations
                            for nucleotide_seq, reads in nucleotides.items():
                                # Iterate through each read and extract features
                                for read in reads:
                                    # Create a dictionary to store features for this read
                                    features = {
                                        'transcript_id': transcript_id,
                                        'transcript_position': pos,
                                        'nucleotide_sequence': nucleotide_seq,
                                        'dwelling_time': read[0],
                                        'std_dev': read[1],
                                        'mean_signal': read[2],
                                        'dwelling_time_flank1': read[3],
                                        'std_dev_flank1': read[4],
                                        'mean_signal_flank1': read[5],
                                        'dwelling_time_flank2': read[6],
                                        'std_dev_flank2': read[7],
                                        'mean_signal_flank2': read[8],
                                    }
                                    # Append the features dictionary to the list
                                    parsed_data.append(features)

                except json.JSONDecodeError as e:
                    print(f"Error parsing line: {e}")

    # Convert the list of parsed data into a DataFrame
    df = pd.DataFrame(parsed_data)
    return df

def aggregate_data(df):
    # Perform aggregation
    aggregated_df = df.groupby(['transcript_id', 'transcript_position']).agg({
        'nucleotide_sequence': 'first',  # Keep the first occurrence
        'dwelling_time': 'mean',
        'std_dev': 'mean',
        'mean_signal': 'mean',
        'dwelling_time_flank1': 'mean',
        'std_dev_flank1': 'mean',
        'mean_signal_flank1': 'mean',
        'dwelling_time_flank2': 'mean',
        'std_dev_flank2': 'mean',
        'mean_signal_flank2': 'mean'
    }).reset_index()
    return aggregated_df

# Main code block
if __name__ == "__main__":
    json_file = "/Users/jheongry/Documents/GitHub/billiegene/data/dataset0.json"
    parsed_df = parse_data(json_file)
    aggregated_df = aggregate_data(parsed_df)
    aggregated_df.to_csv('rf_aggregated2.csv', index=False)
    print("Aggregated data saved to 'rf_aggregated2.csv'")
