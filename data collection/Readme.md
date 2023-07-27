Data collection Group

Task: To provide data from s3 using boto3 
The data is already available as a TSV file.
#needhelp
Need more clear information on how to set up and integrate to use S3 for connecting it with data and fetching it from there.
It would be really helpful if anyone can guide us through

### Details about the data
# Cancer Therapy and Clonal Hematopoiesis (MSK, Nat Genet 2020)

### Data for all types of cancer detection

MSK-IMPACT was used to identify clonal hematopoiesis mutations in blood samples from 24,146 individuals whose tumor-blood pairings were analysed.PubMed

The following cancer types can be identified from the data:
1. Breast Cancer
2. Nerve Sheath Tumor
3. Retinoblastoma
4. Sex Cord Stromal Tumor
5. Miscellaneous Brain Tumor
6. Wilms Tumor 
7. Miscellaneous Neuroepithelial Tumor
8. Vaginal Cancer
9. Gestational Trophoblastic Disease
10. Penile Cancer
11. Pheochromocytoma
12. Pineal Tumor
13. Choroid Plexus Tumor

### The basic explanation for each column in the dataset
1.	**Study ID:** Identifier for the study related to the collected data. Value example: msk_ch_2020
2.	**Patient ID:** Unique identifier for each patient involved in the study. Value example: P-0000015
3.	**Sample ID:** Unique identifier for each sample related to a patient. Value example: P-0000015-N01
4.	**Age:** The patient's age at the time of sample collection. Value example: 44.44079208
5.	**Alkylating Agent Treatment:** Indicates whether the patient received treatment with alkylating agents. Value example: Yes or No
6.	**All therapy at MSKCC:** Indicates whether the patient received all therapy at Memorial Sloan Kettering Cancer Center (MSKCC). Value example: Yes or No
7.	**Anthracycline Treatment:** Indicates whether the patient received treatment with anthracycline agents. Value example: Yes or No
8.	**Antimetabolite Treatment:** Indicates whether the patient received treatment with antimetabolite agents. Value example: Yes or No
9.	**Cancer Type:** The general type of cancer of the patient. Value example: Breast Cancer, Prostate Cancer
10.	**Cancer Type Detailed:** A more detailed description of the patient’s specific cancer type. Value example: Invasive Breast Carcinoma, Prostate Adenocarcinoma
11.	**Carboplatin Treatment:** Indicates whether the patient received treatment with carboplatin. Value example: Yes or No
12.	**Chemotherapy Treatment:** Indicates whether the patient received any form of chemotherapy treatment. Value example: Yes or No
13.	**Cisplatin Treatment:** Indicates whether the patient received treatment with cisplatin. Value example: Yes or No
14.	**Cytotoxic Chemotherapy Treatment:** Indicates whether the patient received any cytotoxic chemotherapy treatment. Value example: Yes or No
15.	**EQD Tertiles:** EQD stands for "Equivalent Dose in 2-Gy Fractions." It is a way to measure and compare the biological effects of different radiation therapy treatments. Value example: 1st tertile, No radiation
16.	**Folic Acid Analog Treatment:** Indicates whether the patient received treatment with folic acid analogs. Value example: Yes or No
17.	**Immunotherapy Treatment:** Indicates whether the patient received immunotherapy treatment. Value example: Yes or No
18.	**Microtubule Damaging Agent:** Indicates whether the patient received treatment with microtubule damaging agents. Value example: Yes or No
19.	**Mutation Count:** The number of mutations detected in the patient's sample. Value example: 1, 2 
20.	**Nucleoside Analogue Treatment:** Indicates whether the patient received treatment with nucleoside analogues. Value example: Yes or No
21.	**Oncotree Code:** Code representing the patient's cancer type based on Oncotree classification. Value example: BRCA, PEMESO, OUTT
22.	**Other Cytotoxic Treatment:** Indicates whether the patient received other forms of cytotoxic therapy. Value example: Yes or No
23.	**Oxaliplatin Treatment:** Indicates whether the patient received treatment with oxaliplatin. Value example: Yes or No
24.	**Platinum Treatment:** Indicates whether the patient received treatment with platinum-based agents. Value example: Yes or No
25.	**Race:** Ethnicity or race of the patient. Value example: White, Asian
26.	**Radiotherapy Treatment:** Indicates whether the patient received radiotherapy treatment. Value example: Yes or No
27.	**Number of Samples Per Patient:** The total number of samples collected for each patient. Value example: 1
28.	**Sex:** Gender of the patient. Value example: Male, Female	 
29.	**Smoking Status:** Indicates the smoking status of the patient. Value example: Never smoker, Current Smoker
30.	**Targeted Therapy Treatment:** Indicates whether the patient received targeted therapy treatment. Value example: Yes or No
31.	**Taxane Treatment:** Indicates whether the patient received treatment with taxane agents. Value example: Yes or No
32.	**Cumulative Exposure to Alkylating Agent:** Cumulative exposure to alkylating agents. Value example: No treatment, 3rd tertile
33.	**Cumulative Exposure to Anthracycline:** Cumulative exposure to anthracycline agents. Value example: No treatment, 3rd tertile
34.	**Cumulative Exposure to Antimetabolite:** Cumulative exposure to antimetabolite agents. Value example: No treatment, 3rd tertile
35.	**Cumulative Exposure to Carboplatin:** Cumulative exposure to carboplatin. Value example: No treatment, 3rd tertile
36.	**Cumulative Exposure to Cisplatin:** Cumulative exposure to cisplatin. Value example: No treatment, 3rd tertile
37.	**Cytotoxic Chemotherapy Treatment Tertile:** Classification of the patient into tertiles based on cytotoxic chemotherapy treatment. Value example: No treatment, 3rd tertile
38.	**Cumulative Exposure to Immunotherapy:** Cumulative exposure to immunotherapy treatment. Value example: No treatment, 3rd tertile
39.	**Cumulative Exposure to Microtubule Damaging Agent:** Cumulative exposure to microtubule damaging agents. Value example: No treatment, 3rd tertile
40.	**Cumulative Exposure to Other Cytotoxic Therapy:** Cumulative exposure to other forms of cytotoxic therapy. Value example: No treatment, 3rd tertile
41.	**Cumulative Exposure to Oxaliplatin:** Cumulative exposure to oxaliplatin. Value example: No treatment, 3rd tertile
42.	**Cumulative Exposure to Platinum:** Cumulative exposure to platinum-based agents. Value example: No treatment, 3rd tertile
43.	**Cumulative Exposure to Targeted Therapy:** Cumulative exposure to targeted therapy treatment. Value example: No treatment, 3rd tertile
44.	**Cumulative Exposure to Taxane:** Cumulative exposure to taxane agents. Value example: No treatment, 3rd tertile
45.	**Cumulative Exposure to Topoisomerase II Inhibitor:** Cumulative exposure to topoisomerase II inhibitor agents. Value example: No treatment, 3rd tertile
46.	**Cumulative Exposure to Topoisomerase I Inhibitor:** Cumulative exposure to topoisomerase I inhibitor agents. Value example: No treatment, 3rd tertile
47.	**Time from Diagnosis:** The time spent from diagnosis to sample collection. The measurement unit is days. Value example: 991, 255
48.	**Time to Blood Draw from Treatment:** The time spent from the start of treatment to blood sample collection. The measurement unit is days. Value example: 609,5
49.	**TMB (nonsynonymous):** Tumor Mutational Burden, the count of nonsynonymous mutations. Value example: 0.066666667
50.	**Topoisomerase II Inhibitor Treatment:** Indicates whether the patient received treatment with topoisomerase II inhibitor agents. Value example: Yes or No
51.	**Topoisomerase I Inhibitor Treatment:** Indicates whether the patient received treatment with topoisomerase I inhibitor agents. Value example: Yes or No
52.	**Treatment Status:** Indicates the treatment status of the patient. Value example: Treated, Unknown
53.	**Radiation Therapy:** Indicates whether the patient received radiation therapy treatment. Value example: Yes or No

### Using data file and the script file 

The data file is [msk_ch_2020_clinical_data.tsv](https://github.com/professor-greebie/SENG8080-3-field_project/blob/main/data%20collection/msk_ch_2020_clinical_data.tsv)

Use the python script file to open the TSV data [Data_read.py](https://github.com/professor-greebie/SENG8080-3-field_project/blob/main/data%20collection/data_read.py).

### Credits
The Credits of the data goes to [cBioPortal_for_Cancer_Genoics]https://www.cbioportal.org/study/summary?id=msk_ch_2020
