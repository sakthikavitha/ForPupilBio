import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load your CSV file into a DataFrame
df = pd.read_csv('PupilBioTest1_PMP_revA.csv')


# Compute the 'Total Coverage' column 
columns_to_sum = ['c000', 'c001', 'c010', 'c011', 'c100', 'c101', 'c110', 'c111'] 
df['Total Coverage'] = df[columns_to_sum].sum(axis=1)
# Print the resulting counts


# Generate a line plot for 'Total Coverage' by 'Sample_ID'
total_coverage_by_sample = df.groupby(['Tissue','Sample_ID'])['Total Coverage'].agg([np.mean, np.median, np.std]).reset_index()
plt.figure(figsize=(10, 6))
plt.plot(total_coverage_by_sample['Sample_ID'], total_coverage_by_sample['Total Coverage'])
plt.title('Total Coverage by Sample_ID')
plt.xlabel('Sample_ID')
plt.ylabel('Total Coverage')
plt.xticks(rotation=45)

output_file = 'lineplot_coverage.jpg'
plt.savefig(output_file, format='jpg')
print(f"Lineplot saved as {output_file}")