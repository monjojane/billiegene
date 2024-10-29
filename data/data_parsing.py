import json
import pandas as pd

def parse_data(json_file):
    # Load the JSON data from the file
    with open(json_file) as f:
        json_data = json.load(f)

    # Initialize an empty list to hold the parsed data
    parsed_data = []

    # Iterate through the transcripts
    for transcript_id, positions in json_data.items():
        # Iterate through each position in the transcript
        for pos, nucleotides in positions.items():
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

    # Convert the list of parsed data into a DataFrame
    df = pd.DataFrame(parsed_data)

    return df

# Example usage
jsonfile = 'dataset0.json'  # Replace with your actual JSON file path
parsed_df = parse_data(jsonfile)
print(jsonfile.head())
print(parsed_df.head())  # Display the first few rows of the parsed DataFrame