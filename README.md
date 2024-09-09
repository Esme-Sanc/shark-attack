# 📊 Shark Attack Analysis with Python

Welcome to the Shark Attack Analysis project! This notebook performs an exploratory data analysis (EDA) on shark attack data using Python's data analysis libraries, like pandas, seaborn, and matplotlib.

## 📊 Notebook Overview 


### 📂 Project Structure

- **Data Loading:** : Reads the dataset from an online source and inspects the basic structure of the DataFrame.
- **Data Exploration:** Looks into the columns, checks for missing values, and explores the basic statistics of the dataset.
- **Data Preprocessing** Cleans the dataset by standardizing column names, filtering relevant rows, handling missing values, and correcting inconsistent entries.
- **Data Visualization:** Provides insights on various aspects, such as attacks by gender, year, and type, with detailed visualizations.

### Dataset Overview

The data for this analysis comes from sharkattackfile.net and contains information about shark attacks worldwide. It includes columns such as the date, year, type of attack (provoked/unprovoked), location, and demographic details like the gender of the victim.


## 📊 Steps in the Notebook

**1. Data Loading:**  

Load the dataset directly from the online source using pandas. Check the shape and inspect the first few rows to understand the structure.

**2. Initial Data Exploration** 

Inspect column names, look at missing values, and check for inconsistencies in the data.

**3. Data Preprocessing**

   o	Standardize column names to lowercase and remove unnecessary columns.
   o	Filter the dataset to retain only relevant years (1994 and beyond).
   o	Handle missing data and clean up invalid entries in key columns like 'gender.'
   
**4. Data Cleaning**

Remove irrelevant columns and adjust data types where necessary.

**5. Data Visualization**

Remove irrelevant columns and adjust data types where necessary.
   o	Gender Analysis: Visualize the number of attacks by gender using bar plots and pie charts.
   o	Yearly Analysis: Show the distribution of attacks over the years using a line plot.

## 📈 Key Visual Insights

•	Gender Analysis: Most shark attacks involved male victims, which is illustrated using both bar and pie charts.
•	Yearly Trends: A clear trend over time, showing how shark attack incidents have varied from 1994 onwards.
![image](https://github.com/user-attachments/assets/2ea79660-e59c-4d2e-be06-cbda3618af9d)
![image](https://github.com/user-attachments/assets/4422e5d6-e8a6-4c8e-bdc9-9837cdd4bd43)
![image](https://github.com/user-attachments/assets/32cea855-01b2-48a6-81ac-48585f31712a)
![image](https://github.com/user-attachments/assets/93c4e14b-8150-4f6a-9730-39a8144c835e)




## 📜 Conclusion
 This analysis showcases how to handle real-world datasets by addressing common challenges such as missing values, inconsistent data, and outliers. The visualizations provide a deeper understanding of trends in shark attacks.
 The data shows that shark attacks have increased in the past 30 years, attacks are higher and more deadly in men.

## 🧑‍💻 Authors
This project was developed by Esme Rodriguez, Elena Vilkoyt, Irene Sifre
