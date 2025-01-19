import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load your CSV file into a DataFrame
alldf = pd.read_csv('PupilBioTest1_PMP_revA.csv')

# Filter rows where 'Tissue' is 'cfDNA' or 'Sample_ID' is 1 
df = alldf[(alldf['Tissue'] == 'cfDNA') | (alldf['Sample_ID'] == 1)]


# Compute the 'Total Coverage' column 
columns_to_sum = ['c000', 'c001', 'c010', 'c011', 'c100', 'c101', 'c110', 'c111'] 
df['Total Coverage'] = df[columns_to_sum].sum(axis=1)
# Print the resulting counts



# Let's assume 'CpG Coordinates' needs preprocessing to extract numerical values
df['CpG Start'] = df['CpG_Coordinates'].apply(lambda x: int(x.split(':')[1]))

# Generate a scatter plot for 'Total Coverage' vs. 'CpG Start'
plt.figure(figsize=(10, 6))
plt.scatter(df['CpG Start'], df['Total Coverage'])
plt.title('Total Coverage vs. CpG Start')
plt.xlabel('CpG Start')
plt.ylabel('Total Coverage')
plt.show()



output_file = 'scatterplot_coverage.jpg'
plt.savefig(output_file, format='jpg')
print(f"Scatterplot saved as {output_file}")