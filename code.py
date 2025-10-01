#Average admissions per month
import pandas as pd
df = pd.read_csv("healthcare_dataset.csv")

#admission dates to datetime
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], format='%m/%d/%Y')

# Extracting year and month
df['Year_Month'] = df['Date of Admission'].dt.to_period('M')

# admissions per month
monthly_admissions = df['Year_Month'].value_counts().sort_index()

# DataFrame
monthly_df = pd.DataFrame({
    'Month': monthly_admissions.index.astype(str),
    'Admissions': monthly_admissions.values
})

monthly_df


#Average Discharges per year
import pandas as pd

# Get the healthcare dataset
df = pd.read_csv("healthcare_dataset.csv")

# discharge dates to datetime
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'], format='%m/%d/%Y')

# Extracting year 
df['Discharge_Year'] = df['Discharge Date'].dt.year

# discharges per year
yearly_discharges = df['Discharge_Year'].value_counts().sort_index()

#  average discharges per year
complete_years = yearly_discharges[yearly_discharges.index <= 2023]
average_discharges = complete_years.mean()

# DataFrame
summary = pd.DataFrame({
    'Metric': ['Average Discharges per Year (2019-2023)', 'Total Complete Years', 'Total Discharges (Complete Years)', 'Lowest Year', 'Highest Year'],
    'Value': [f"{average_discharges:.0f}", f"{len(complete_years)}", f"{complete_years.sum()}", f"{complete_years.min()}", f"{complete_years.max()}"]
})

summary

#Doctor-to-patient ratio
import pandas as pd

# Get the healthcare dataset
df = pd.read_csv("healthcare_dataset.csv")

# unique doctors
unique_doctors = df['Doctor'].nunique()

# total admissions
total_patients = len(df)

# doctor to patient ratio
doctor_patient_ratio = (total_patients) / (unique_doctors)

# DataFrame
summary = pd.DataFrame({
    'Metric': ['Unique Doctors', 'Total Patients', 'Doctor to Patient Ratio', 'Patients per Doctor'],
    'Value': [f"{unique_doctors}", f"{total_patients}", f"1:{doctor_patient_ratio:.1f}", f"{doctor_patient_ratio:.1f}"]
})

summary

#Average admissions per year
import pandas as pd

# Get the healthcare dataset
df = pd.read_csv("healthcare_dataset.csv")

# admission dates to datetime
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], format='%m/%d/%Y')

# Extracting year 
df['Year'] = df['Date of Admission'].dt.year

# admissions per year
yearly_admissions = df['Year'].value_counts().sort_index()

# average admissions per year
complete_years = yearly_admissions[yearly_admissions.index <= 2023]
average_admissions = complete_years.mean()

# DataFrame
summary = pd.DataFrame({
    'Metric': ['Average Admissions per Year (2019-2023)', 'Total Complete Years', 'Total Admissions (Complete Years)', 'Lowest Year', 'Highest Year'],
    'Value': [f"{average_admissions:.0f}", f"{len(complete_years)}", f"{complete_years.sum()}", f"{complete_years.min()}", f"{complete_years.max()}"]
})

summary
