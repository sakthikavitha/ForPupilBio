import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file into a DataFrame
alldf = pd.read_csv('PupilBioTest1_PMP_revA.csv')
# Filter rows where 'Tissue' is 'cfDNA' or 'Sample_ID' is 1 
df = alldf[(alldf['Tissue'] == 'cfDNA') ]
# Group by 'Sample_ID' and count the number of records
#sample_counts = df.groupby('Sample_ID').size().reset_index(name='Total_Records')

# Group by 'Tissue' and count the number of records
#sample_counts = df.groupby('Tissue,Sample_ID').size().reset_index(name='Total_Records')
#sample_counts = df.groupby(['Tissue', 'Sample_ID']).size().reset_index(name='Total_Records')

# Save the result to a new CSV file
#sample_counts.to_csv('sample_counts.csv', index=False)

# Compute the 'Total Coverage' column 
columns_to_sum = ['c000', 'c001', 'c010', 'c011', 'c100', 'c101', 'c110', 'c111'] 
df['Total Coverage'] = df[columns_to_sum].sum(axis=1)
# Combine 'Tissue' and 'Sample_ID' into a new column 
#df['Tissue_SampleID'] = df['Tissue'] + '_' + df['Sample_ID'].astype(str)
# Print the resulting counts
# print(sample_counts)
# Generate a boxplot for the 'Total Coverage' column
plt.figure(figsize=(20,10))
#-----------------------------------------------------
df.boxplot(column='Total Coverage', by='Sample_ID', whis=1.5, showmeans=True)
plt.title('Boxplot of Total Coverage by Tissue')
plt.suptitle('')  # Remove the automatic 'Boxplot grouped by' title
plt.xlabel('Sample_ID')
plt.ylabel('Total Coverage')
plt.xlim(-2, len(df['Sample_ID'].unique()) + 2)
plt.xticks(rotation=45)
#plt.show()
# Save the boxplot as a .jpg file
output_file = 'boxplot_tissue_sampleid_total_coverage.jpg' 
plt.savefig(output_file, format='jpg')
#-----------------------------------------------------


print(f"Boxplot saved as {output_file}")