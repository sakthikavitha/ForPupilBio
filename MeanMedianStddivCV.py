import pandas as pd
import numpy as np

# Load your CSV file into a DataFrame
#df = pd.read_csv('ip_first1000cpg.csv')PupilBioTest1_PMP_revA.csv
df = pd.read_csv('PupilBioTest1_PMP_revA.csv')

# Define the columns to aggregate
columns_to_aggregate = ['c000', 'c001', 'c010', 'c011', 'c100', 'c101', 'c110', 'c111']

# Aggregate the specified columns and calculate the results
df['aggregated'] = df[columns_to_aggregate].sum(axis=1)

# Group by the 'Tissue' column and calculate mean, median, standard deviation, and CV
result = df.groupby('Tissue')['aggregated'].agg([np.mean, np.median, np.std])
result['cv'] = result['std'] / result['mean']  # Calculate CV

# Save results to a new CSV file (optional)
result.to_csv('aggregated_statistics_with_cv.csv')

# Display the result
print(result)