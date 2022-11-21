# Age-sex-adjusted rate
🔀 An age-gender-adjusted rate is one of the most useful summary statistics for comparing the impact of diseases that are heavily influenced by age and gender across different populations.

This repository includes a Python function that calculates the age and sex standardised estimates for a certain disease and/or list of diseases. It also calculates a 95% confidence interval for each estimate.

The calculated estimates of diseases can be then used to compare with other estimates of diseases to assess the impact of the disease.

This function uses the 2021 England Census as a standard population to determine the percentage for each age-gender group by 10-year age group. You can download the census data from the Office for National Statistics’ s website (found at https://www.ons.gov.uk/census).

# Steps for calculating the age-gender-adjusted rate:
**Step 1: Break up the population:**

Divide the population into age and gender groups, and then find the total number of cases and the matching age and gender group population.

**Step 2: Calculate age-gender specific rate for each age-gender group:**

Divide the number of cases by each group's total population and then multiply that number by either 100, 1000, 10000, or 100000. This gives an age-gender specific rate per the chosen population size.

This function uses a 10000 population size.

**Step 3: Choose a standard population**

Find the percentage of the standard population for each age-gender group.

**Step 4: Calculate the weighted age-gender specific rate for each age-gender group:**

Multiply each age-gender specific rate by the percent of the standard population for each age-gender group.

**Step 5: Find the total of the weighted age-specific rates**

Add up the weighted age-specific rates calculated in step 4. The sum of these values is the age-gender adjusted rate for that group of the dataset.

**Step 6: Calculate the 95% CI for the estimates**

The formula used in this script is as follows:

SE = R / square root of N

where:

R = (age-sex-adjusted) rate

N = number of events (cases)

SE = standard error

The estimated SE can then be used to compute a 95% confidence interval (CI) for the rate. The
standard formula for determining the 95% CI of a rate is:

CI = R ± (1.96 x SE)

# Input data
In order for this function to work, you need three prepared datasets that can be analysed and merged in the process. 

The estimates are calculated based on three input datasets: 1) participants, 2) diseases and 3) census

## Exemplar datasets for calculating the age-sex-adjusted rate

### Participants data
An example of participants data is given below.


| participant_id | sex | age group | 
| ------------- | ------------- | ------------
| 1 | male | 30-39 |
| 2 | female | 40-49 |
| 3 | male | 20-29 |
| 4 | female | 60-69 |
| 5 | male | 45-59 |

### Diseases data
An example of diseases data is given below.


| participant_id | disease |
| ------------- | ------------- |
| 1 | asthma |
| 1 | diabetes |
| 2 | diabetes |
| 2 | obesity |
| 2 | hypertension |
| 3| asthma |
| 3 | diabetes |
| 4 | obesity |
| 5 | hypertension |
| 5 | diabetes |

### Census data
An example of census data (2021 English census data) is given below.

| age group | sex | percentage | 
| ------------- | ------------- | ------------
| 0_9 | male | 0.06
| 0_9	| female | 0.06
| 10_19 | male | 0.06
| 10_19	| female |	0.06
| 20_29 | male |0.06
| 20_29 | female |0.06


# Output

One text file with all the results (prevalence of diseases) will be written out as dataframe. Also, the results will be printed out as strings in the output section. 

Please note that the output numbers and estimates may not be realistic as this is just an example to show how the function works.

An example of a printed output data is given below:


Age-sex-adjusted prevalence for ['asthma'] is 1300.0 per 10,000 ( 1171.1 , 2771.1 )


Age-sex-adjusted prevalence for ['diabetes '] is 1850.0 per 10,000 ( 228.4 , 3471.6 )


Age-sex-adjusted prevalence for ['hypertension'] is 3150.0 per 10,000 ( 967.2 , 5332.8 )


Age-sex-adjusted prevalence for ['depression'] is 2450.0 per 10,000 ( 489.6 , 4410.4 )


An example of a written text file is given below:

| disease | Age-sex-adjusted prevalence | CI | 
| ------------- | ------------- | ------------
| asthma | 1300.0 | 1171.1 , 2771.1 
| diabetes	| 1850.0 | 228.4 , 3471.6 
| hypertension | 3150.0 | 967.2 , 5332.8
| depression	| 2450.0 | 489.6 , 4410.4

