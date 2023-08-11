# ColombiaTrans-Insights
Brief description: Dispatches, passengers, and beyond: Comprehensive analysis of public transportation in Colombia. Understand travel patterns with processed data and generated tables.
# Examples:
<img src="https://github.com/Pking31/ColombiaTrans-Insights/blob/8bc4f7b7b14cc37299f0d2f7b4f47d10ee1984ae/images/tend.png" alt="Texto alternativo" >
<img src="https://github.com/Pking31/ColombiaTrans-Insights/blob/8bc4f7b7b14cc37299f0d2f7b4f47d10ee1984ae/images/clases.png" alt="Texto alternativo">

# Project Summary
This project focuses on the exploration and analysis of public transportation data using Python and the pandas, sodapy, and gspread libraries. The data was sourced from the Socrata API of "datos.gov.co". The main objective is to understand patterns, trends, and features related to dispatches and passengers on public transportation routes.

# Project Contents

1. Data Loading and Table Merging: Data is downloaded from the API and combined with additional information about the origin and destination municipalities. Pagination adjustments are made, and a "data" DataFrame is constructed.
2. Initial Exploratory Analysis: Data is loaded into a new DataFrame "df". Records with passengers greater than 0 are filtered in "power_bi". Statistical analysis is conducted, and missing values are detected.
   
3. Analysis by Year and Department: Data is grouped by year and origin department to calculate the number of dispatches. The "dispatches_departments_per_year" table is created.
   
4.Analysis by Month and Department: Data is grouped by month and department to obtain the monthly dispatch count.

5.Popular Routes and Dispatches: Tables are generated showcasing the most popular routes based on passengers and dispatches.

6. Average Passengers per Class: The average number of passengers per vehicle class is calculated.
   
8. Analysis by Day of the Week: Dispatches and passengers are analyzed based on the day of the week.
   
10. Analysis by Hour and Month: Dispatches are studied by dispatch hour and month.
 
12. Service Level and Passengers: Service level is analyzed in relation to the passenger count.
    
14. Export to Google Sheets: A script is included that authenticates with JSON credentials, loads data from CSV files to Google Sheets, and creates or updates sheets as needed.

# Using the Results
Analysis and manipulation results are exported as CSV files for further analysis, visualization, or integration into tools like Power BI. Additionally, a script is provided to upload this data to Google Sheets, facilitating collaboration and access to results.

# Requirements and Usage

Python 3.x
Libraries: pandas, sodapy, gspread, and oauth2client
Download data from the official source and DIVIPOLA_Municipios
Configure GSuite credentials locally to upload tables to Google Sheets
Utilize the provided modular code to upload results to Google Sheets
# Dashboard Power BI
<img src="https://github.com/Pking31/ColombiaTrans-Insights/blob/20fccb039318a00c2d04bbaaf2e271b811c90ef8/images/dashboard.png" alt="Texto alternativo" width="500" height="400">
