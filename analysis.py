# This Python script is for the project regarding HPV vaccination coverage amongs adolescent girls in 6 European countries from 2010-2023


import pandas as pd ## importing pandas to load, filter and analyse data stored as tables 
import matplotlib.pyplot as plt ## importing matplotlib to create plots and visualise the results 
from scipy.stats import skew, kurtosis ## using scipy.states we are importing skew, kurtosis (2/4 of our descriptive statistics we want to analyse)


## STEP 1: Loading the relevant dataset

# Here we will be loading the CSV dataset from the data folder into a pandas DataFrame
# A DataFrame is a table with rows and columns of data 
df = pd.read_csv("data/hpv_vaccination.csv")

print("Dataset loaded successfully!") # Printing a confirmation message 
print("Shape:", df.shape) # 'Shape' tells us the number of rows and columns 

# Here we display the column names to identify which variables we want to use 
print("\nColumns:") 
print(df.columns)


# Step 2: Selecting countires & years 

## Here we list the 6 European countries this project focuses on 
countries = [
    "Netherlands",
    "Belgium",
    "Germany",
    "France",
    "Spain",
    "Sweden"
]
# Here we store the exact column name containing the HPV Vaccination coverage 
coverage_col = "HPV Vaccination coverage by age 15, last dose, females"

# Only keeping the observations from the selected countries and the years 2010-2023 
df = df[
    (df["Entity"].isin(countries)) & ## is.in checks whether a country appears in our selectedcountry range 
    (df["Year"].between(2010, 2023)) ## between selects years within the specified range including the 2 endpoints 
]

# This line removes rows where vaccination coverage is missing preventing any missing values from impacting the calculations 
df = df.dropna(subset=[coverage_col])

# Step 3: Check the data

## Here we count how many observations are available for each country 
print("\nNumber of observations per country:")
print(df.groupby("Entity").size())

# Here we count the number of different countries with data in each year helping identify years with incomplete country coverage 
print("\nNumber of countries per year:")
print(df.groupby("Year")["Entity"].nunique())

# These lines check the earliest and latest years remain after filtering
print("\nYears:")
print(df["Year"].min(), "to", df["Year"].max())

# Step 4: Calculating Mean and STDEV 

# Here we group the data by year to compare vaccination coverage over time
# We do this to calculate the mean and standard deviation for each year 
summary = (
    df.groupby("Year")[coverage_col]
    .agg(
        mean="mean",
        std="std"
    )
    .reset_index()
)
# Here we display the yearly summary statistics in the terminal 
print("\nMean and standard deviation:")
print(summary)

# Step 5: Plotting the mean and STDEV 

plt.figure(figsize=(10, 6))

# Here we plot the mean vaccination coverage as a line with circular markers
plt.plot(
    summary["Year"],
    summary["mean"],
    marker="o",
    linewidth=2,
    label="Mean"
)
# These lines of code are used to shade the area between the mean minus 1 STDEV and plus 1 STDEV
plt.fill_between(
    summary["Year"],
    summary["mean"] - summary["std"],
    summary["mean"] + summary["std"],
    alpha=0.2,
    label="± 1 standard deviation"
)

# Here we add labels and a descriptive title to the graph 
plt.xlabel("Year")
plt.ylabel("HPV vaccination coverage (%)")

plt.title(
    "HPV vaccination coverage in six European countries"
)
## Here we display a tick ever 2 years for the horizonal axis 
plt.xticks(range(2010, 2024, 2))

# These lines are to show the legend, grid and improve the spacing 
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Here we can save the plot as a PNG in the figures folder  
plt.savefig(
    "figures/mean_sd_hpv.png",
    dpi=300
)

# Displaying the plot 
plt.show()

# Step 6: Calculating the skewness & excess kurtosis 

## Here we calculate the shape of the vaccination coverage distribution for each year 
# Excess kurtosis is used to describe tail heaviness in comparison to a normal distribution (bell)
shape = (
    df.groupby("Year")[coverage_col]
    .agg(
        skewness=lambda x: skew(x, bias=False),
        kurtosis=lambda x: kurtosis(x, bias=False)
    )
    .reset_index()
)
# Here we print the results for every year
print("\nSkewness and kurtosis:")
print(shape)


# Step 7: Plotting the skewness and kurtosis 

plt.figure(figsize=(10, 6))

# Here we plot the yearly skewness values 
plt.plot(
    shape["Year"],
    shape["skewness"],
    marker="o",
    linewidth=2,
    label="Skewness"
)

# Here we plot the yearly excess kurtosis values 
plt.plot(
    shape["Year"],
    shape["kurtosis"],
    marker="o",
    linewidth=2,
    label="Excess kurtosis"
)

# These lines of code adds a horizontal reference line at zero to help with identifying positive and negative values 
plt.axhline(
    0,
    linestyle="--",
    linewidth=1
)

# Here we label the axes 
plt.xlabel("Year")
plt.ylabel("Statistic value")
# Here we give the graph a descriptive title 
plt.title(
    "Distribution of HPV vaccination coverage"
)

# This line helps with displaying the labels at two-year intervals 
plt.xticks(range(2010, 2024, 2))

# The following lines add a legend and grid, and adjust the layout further 
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Here we can save the plot as a PNG in the figures folder  
plt.savefig(
    "figures/skewness_kurtosis_hpv.png",
    dpi=300
)
# Displaying the second plot 
plt.show()

# Here we confirm that the analysis script has reached the end 
print("\nAnalysis completed successfully!")