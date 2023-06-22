#This Program will open TSV file as dataframe for better analysis.
import pandas as pd
# Importing Data
filename = r"C:\Users\rajan\Downloads\luad_mskcc_2023_met_organotropism_clinical_data.tsv" #Enter file path

df = pd.read_csv(filename,sep='\t') # store as df From a TSV file
pd.set_option('display.max_columns', None)
# Display Data
print(df.head(5))
