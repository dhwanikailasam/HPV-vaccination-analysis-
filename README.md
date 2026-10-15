# HPV-vaccination-analysis- [README.md]

1. Project description: What does the code do and what results it produces

This project is focused on the analysis of the distribution of HPV (human papillomavirus) vaccination among adolescent girls in 6 European countries: The Netherlands, Belgium, Germany, France, Spain and Sweden 

The aim of this project is to investigate how the HPV vaccination coverage varied over time ( in the 6 European countries) between 2010 and 2023.

The project uses Python to calculate 4 descriptive statistic: 
Mean: The average HPV vaccination coverage across the six countries in each year
SD: Quantifies how much the vaccination coverage varies between the countries
Skewness: Measures the asymmetry of the distribution 
Excess kurtosis: Describes the tail behaviour of the distribution and its tendency to contain extreme values (find a better definition) 

Research Question: 
How did HPV Vaccination coverage among adolescent girls change between 2010 and 2023 in the Netherlands, Belgium, Germany, France, Spain and Sweden? 

The python script is expected to produce 2 plots:
Plot 1: (MEAN AND SD) A line plot showing the annual mean vaccination coverage with a shaded band representing one standard deviation and below the mean
Plot 2 (Skewness & Excess Kurtosis) A line plot showing how the shape of the distribution across the six countries changes over time 

The script prints the calculated statistics in the terminal 

2. Installation: What software or libraries need to be installed

This project requires:
Python 3
Visual Studio Code (VS code)
The Python extension for VS code
The following Python libraries: 
pandas: used for data loading and processing
matplotlib: used for creating plots
scipy: calculating skewness and kurtosis 

The required libraries can be installed in the VS code terminal: python3 -m pip install pandas matplotlib scipy

3. Execution: The commands needed to run the code
	
Download the CSV file form the OWID dataset page
Save it in the data/folder and rename it 

Open a new terminal in VS code and run:  python3 -m pip install pandas matplotlib scipy
Ensure the terminal is in the project directory and then run: python3 analysis.py
The terminal should display the calculated statistics
The script should save the plots in figures/folder as PNGS
The plots may also open in separate windows depending on the local Python environment 

4. Dataset: Where to find the data: how to download or access it: whether any cleaning or preprocessing is needed

The dataset is published by Our World in Data (OWID) and is based on HPV vaccination coverage figures from the WHO and UNICEF
the specific indicator used is: HPV Vaccination coverage by age 15, last dose, females

This measures HPV vaccination coverage among females by age 15 based on the final-dose indicator reported in the dataset 
Countries: The Netherlands, Belgium, Germany, France, Spain and Sweden
Year: 2010-2023 

Data preparation: (within the script) 
Loading the CSV file using pandas
Selecting the 6 specified countries
Filtering the observations to the specified range of years (2010-2023) 
Removing the observations with missing vaccination coverage values 
Groups the observations by year: calculates the 4 descriptive statistics
Generates and saves the 2 plots 

Note: The number of countries with available data may vary by year: The analysis should check the number of countries represented every year before interpreting the results 

Project structure: 
Create a folder on your desktop called “hpv project”
Within “hpv project” create 2 folders: “data” and “figures”

Project directory should have the following structure: 
hpv project/
├── analysis.py
├── README.md
├── MAT2007_HPV_PROJECT__DHWANI_.pdf
├── data/
│   └── hpv_vaccination.csv
└── figures/
    ├── mean_sd_hpv.png
    └── skewness_kurtosis_hpv.png
5. Conditions: Any requirements or assumptions such as a specific Python version, file paths or access permissions 

The script requires Python 3 and the listed libraries
CSV file must be located at data/hpv_vaccination/.csv (within folders)
Figures/directory should exist before running the script (!)
Input CSV file must contain the following columns: Entity, Year and HPV Vaccination coverage by age 15, last dose, females
The analysis only uses available observations and excludes missing coverage values
Calculations do not aim to describe the variation between individual girls
Skewness and kurtosis estimated based on only 6 countries can be unstable (interpret with caution)
The findings applied to the 6 selected countries should not be generalised to all European countries 

