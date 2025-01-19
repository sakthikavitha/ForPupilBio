import pandas as pd
import matplotlib.pyplot as plt


# Load your CSV file into a DataFrame
df = pd.read_csv('PupilBioTest1_PMP_revA.csv')


# Compute the 'Total Coverage' column 
columns_to_sum = ['c000', 'c001', 'c010', 'c011', 'c100', 'c101', 'c110', 'c111'] 
df['Total Coverage'] = df[columns_to_sum].sum(axis=1)
# Print the resulting counts

# Generate a bar plot for 'Total Coverage' by 'Tissue'
total_coverage_by_tissue = df.groupby('Tissue')['Total Coverage'].sum().reset_index()
total_coverage_by_tissue.plot(kind='bar', x='Tissue', y='Total Coverage', legend=False, figsize=(10, 6))
plt.title('Total Coverage by Tissue')
plt.xlabel('Tissue')
plt.ylabel('Total Coverage')
plt.xticks(rotation=45)

output_file = 'barplot_coverage.jpg'
plt.savefig(output_file, format='jpg')
print(f"Barplot saved as {output_file}")