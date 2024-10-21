import json
import pandas as pd

# Initialize an empty list to store the flattened data
flattened_data = []

# Open the file and load each JSON object line-by-line
with open('dataset2.json', 'r') as f:
    for line in f:
        try:
            # Parse each line as a separate JSON object
            data = json.loads(line)

            # Flattening the JSON data into a list of rows
            for transcript_id, positions in data.items():
                for position, sequences in positions.items():
                    for seq, features_list in sequences.items():
                        for features in features_list:
                            row = [transcript_id, position, seq] + features
                            flattened_data.append(row)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON on line: {line}")
            print(e)

# Define the columns for the DataFrame
columns = ['Transcript_ID', 'Position', 'Sequence', 
           'Dwelling_time1', 'Std_dev_signal1', 'Mean_signal1', 
           'Dwelling_time2', 'Std_dev_signal2', 'Mean_signal2', 
           'Dwelling_time3', 'Std_dev_signal3', 'Mean_signal3']

# Create a DataFrame from the flattened data
df = pd.DataFrame(flattened_data, columns=columns)

# Change the position dtype to integer
df['Position'] = df['Position'].astype(int)

# Display the first few rows of the DataFrame
print(df.head())
print(df.info())

# Save the dataframe as csv
df.to_csv('data2_parsed.csv', index=False)