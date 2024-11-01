import json
import pandas as pd

# Parsing raw data so it is in a readable format
def parse_data(json_file):
    parsed_data = []

    with open(json_file, 'r') as f:
        for line in f:
            if line.strip():
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
                                    parsed_data.append(features)

                except json.JSONDecodeError as e:
                    print(f"Error parsing line: {e}")

    # Convert the list of parsed data into a DataFrame
    df = pd.DataFrame(parsed_data)
    return df

def aggregate_data(df):
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


json_file = "../data/sample_data.json" # path to json file you want to parse
parsed_df = parse_data(json_file)
aggregated_df = aggregate_data(parsed_df)
aggregated_df.to_csv('parsed_sample_data.csv', index=False)
print("Aggregated data saved to 'parsed_sample_data.csv'")
