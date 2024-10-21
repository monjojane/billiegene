import pandas as pd

# Load the dataset
df = pd.read_csv('merged1_parsed.csv')

# Add new features
df['Sum_Dwelling_Time'] = df[['Dwelling_time1', 'Dwelling_time2', 'Dwelling_time3']].sum(axis=1)
df['Abs_SD1_SD2'] = abs(df['Std_dev_signal1'] - df['Std_dev_signal2'])
df['Abs_SD1_SD3'] = abs(df['Std_dev_signal1'] - df['Std_dev_signal3'])
df['Abs_SD2_SD3'] = abs(df['Std_dev_signal2'] - df['Std_dev_signal3'])

df['dwelling_time_2_IQ'] = df.groupby(['gene_id', 'transcript_id', 'transcript_position'])['Dwelling_time2'].transform(
    lambda x: x.quantile(0.75) - x.quantile(0.25)
)

# Perform aggregation
aggregated_df = df.groupby(['transcript_id', 'transcript_position']).agg({
    'gene_id': 'first',  # Keep the first occurrence
    'label': 'first',  # Keep the first occurrence
    'Sequence': 'first',  # Keep the first occurrence
    'Dwelling_time1': 'mean',
    'Std_dev_signal1': 'mean',
    'Mean_signal1': 'mean',
    'Dwelling_time2': 'mean',
    'Std_dev_signal2': 'mean',
    'Mean_signal2': 'mean',
    'Dwelling_time3': 'mean',
    'Std_dev_signal3': 'mean',
    'Mean_signal3': 'mean',
    'Sum_Dwelling_Time': 'mean',
    'Abs_SD1_SD2': 'mean',
    'Abs_SD1_SD3': 'mean',
    'Abs_SD2_SD3': 'mean',
    'dwelling_time_2_IQ': 'first'
}).reset_index()

# Save the aggregated DataFrame with new features to a CSV file
aggregated_df.to_csv('aggregated_new.csv', index=False)
