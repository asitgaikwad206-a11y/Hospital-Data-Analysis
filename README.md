🏥 Hospital Data Analysis Project
🎯 Project Overview
This project involves a comprehensive analysis of hospital data to extract meaningful insights that can help improve operational efficiency, patient care quality, and resource allocation. The entire process, from raw data to interactive dashboards, was executed using Google Sheets, Python (for Exploratory Data Analysis), and Tableau (for visualization).

📊 Data Source
The dataset used for this analysis includes:

Source: [Insert Actual Data Source, e.g., Kaggle, internal data (if public and permissible), synthetic data]

File(s): hospital and analysis.csv, healthcare_dataset.csv, etc.,compressed_data.csv.gz

Description: The data includes fields such as patient demographics, admission and discharge details, procedure costs, length of stay, and insurance coverage.

🛠️ Tools Used
Phase	Tool	Purpose
Data Cleaning & Validation	Google Sheets	Initial cleaning, validation checks, and data manipulation.
Exploratory Data Analysis (EDA)	Python (Pandas, NumPy, Matplotlib, Seaborn)	Deep dive into data patterns, statistical analysis, and feature engineering.
Visualization & Reporting	Tableau	Creating interactive dashboards and final insights reporting.

Export to Sheets
🧹 Phase 1: Data Cleaning & Validation in Google Sheets
The initial data preparation was performed directly in Google Sheets due to its effective in-built tools for quick review and data validation.

Data Cleaning Steps
Handled Missing Values: Used filtering to quickly identify and fill or remove rows with missing critical data (e.g., a missing 'Discharge Date' for a discharged patient).

Removed Duplicates: Utilized the "Remove duplicates" feature under the Data > Data Cleanup menu to ensure all patient records were unique.

Standardized Text Fields: Used functions like LOWER() and PROPER() to ensure consistent case for categorical fields (e.g., 'Gender', 'Admission Type').

Tidied Date Formats: Ensured all date columns (e.g., 'Admission Date', 'Discharge Date') were in a uniform YYYY-MM-DD format.

Data Validation Checks
Data Validation Rules: Applied Data Validation rules (under Data menu) to critical columns to enforce consistency:

Length of Stay: Created a custom formula validation to ensure 'Discharge Date' ≥ 'Admission Date'.

Categorical Fields: Used 'List of items' validation for columns like 'Gender' and 'Admission Type' to restrict entries to a predefined list (e.g., Male, Female, Emergency, Elective).

Checked for Outliers: Employed conditional formatting to visually flag any extreme values in numerical columns like 'Hospital Charge' and 'Patient Age', confirming them against known ranges.

🐍 Phase 2: Exploratory Data Analysis (EDA) in Python
Once the data was clean, it was loaded into a Jupyter Notebook for in-depth statistical analysis and pattern discovery using Python libraries like Pandas, NumPy.

Key Analytical Calculations and Insights
We performed time-series and ratio-based analyses to uncover operational insights:

Time-Based Admissions & Discharges Analysis

Admissions/Discharges per Year/Month: We converted date fields to datetime objects and used Pandas' resampling/grouping functions to calculate the total and average number of admissions and discharges for each year and month. This helped identify seasonal trends or year-over-year operational changes.

Code Snippet Example (Conceptual):

Python

# Average Admissions per Month
admissions_monthly = df.groupby(df['Admission Date'].dt.to_period('M')).size().mean()
# Admissions per Day Trend
admissions_daily_trend = df.groupby(df['Admission Date'].dt.date).size()
Admissions per Day: Calculated the daily patient volume to assess consistency and identify peak load days.

Resource Allocation Ratios

Doctor-to-Patient Ratio: This critical metric was calculated to assess staffing levels and potential strain on medical resources.

Formula (Conceptual): Total Active Doctors/Average Daily Patient Count

Bed Occupancy Rate: Analyzed the utilization of hospital resources by calculating the average number of occupied beds over time.

Feature Engineering & Statistical Summaries

Calculated Length of Stay (LOS): LOS=Discharge Date−Admission Date.

Statistical Analysis of Charges: Used df['Hospital Charges'].describe() and applied grouping to understand the mean, median, and variance of costs based on factors like 'Procedure Type' and 'Insurance Payer'.

Visualizations for Pattern Discovery
We used the calculated metrics to generate targeted plots:

Time-Series Plot: Admissions/Discharges over time to visualize trends and seasonality.

Distribution Plots: Histograms/KDE plots for Length of Stay and Charges to identify their distribution shape and skewness.

Comparative Bar Charts: Doctor-to-Patient Ratio and Bed Occupancy Rate broken down by Hospital Wing/Department.

📈 Phase 3: Visualization and Dashboards in Tableau
The final, refined dataset was connected to Tableau to create dynamic and insightful visualizations for stakeholders.

Key Visualizations Created
Total Admissions Trend: Line chart showing admissions over time.

Length of Stay Distribution: Box plot to show the median and spread of LOS by medical department.

Hospital Charges Breakdown: Bar chart or treemap comparing average charges by procedure or insurance type.

Final Dashboard
The primary output is an interactive dashboard designed to answer key business questions, such as: What are the primary drivers of long Length of Stay? and How do average charges vary across different patient segments?

Dashboard Name: [Hospital Dashboard]

Description of Dashboard Image 1:The actual dashboard comprises of few KPI's and donut charts representing the bloodgroups, insurance companys based on the type of admissions, gender, most vital disease seen, count and description of race etc

<img width="786" height="599" alt="image" src="https://github.com/user-attachments/assets/ba592b63-a0ff-4ec1-b4ab-0ce17d62246b" />


Description of Dashboard Image 2:A table where patients every possible information is displayed for example. patient_id,gender,disease,length of stay,satisfactory score, readmissions etc

<img width="770" height="585" alt="image" src="https://github.com/user-attachments/assets/0559f8ea-6015-4529-8993-ef3b1131732e" />
