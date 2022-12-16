# Age-sex-adjusted rate
**Age and sex adjusted rates** are a useful summary statistics for comparison of disease/morality frequency across different populations.

This repository includes a Python function to calculates age and sex standardised estimates (including 95% confidence intervals (CI)) for any disease and/or list of diseases. The calculated adjusted rates can then be used for comparison to other estimates to assess the impact of the disease(s) in a certain population.

In the example usage of this function, the standard population used is the [2021 England Census](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationandhouseholdestimatesenglandandwalescensus2021) data, which is used to determine the percentage for each age(10-year bins) and sex stratified group.

# Calculating the age-sex-adjusted rate:
The following steps are taken.

1. Stratify the population
   - Divide the sample into age and sex stratified groups, and calculate the number of affected (with a given condition) in each group.

2. Calculate the age-sex specific rate for each age-sex group
   - Divide the number of affected by the number of samples in each age-sex stratified group and multiply that with the desired population denominator.
   - In the given example we use 10.000, given a final adjusted rate of **X** affected per 10.000.
   - Other studies report rates per 100.000, change the denominator here to suite the purpose. 

3. Choose a standard population
   - Find the percentage of samples for each age-sex group in a given standard population.
   - Standard population data are made avilable from national census or statistical offices or from regional or international bodies (examples below).
	 - [The European Standard Population](https://www.opendata.nhs.scot/dataset/standard-populations)
	 - [The UK census data](https://www.ons.gov.uk/census)

4. Calculate the weighted age-sex specific rate for each age-sex group
   - Multiply each age-sex specific rate by the percent of that group from the standard population.

5. Sum up the total of the weighted age-sex-specific rates
   - Add up all weighted age-specific rates calculated in step 4. 
   - The sum of these values gives the age-sex adjusted rate for individuals affected in the dataset.

6. Calculate the 95% CI  for the estimates
   - The CIs are calcualted using the following formular.


$$ SE = {R \over\sqrt{N}} $$

where:

**SE** = standard error

**R** = (age-sex-adjusted) rate

**N** = number of events (cases)

The estimated $$SE$$ can then be used to compute a 95% CI for the rate. The
standard formula for determining the 95% CI of a rate is:

$$CI = {R \pm (1.96 x SE)}$$


# Input data
The estimates are calculated based on three input datasets: 1) participants, 2) diseases and 3) census.
Refer to the data folder for more information on each dataset.

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

One text file with all the results (prevalence of diseases) will be written out as dataframe. Also, the results will be printed out as strings in the output section. Note that the examplar data is synthetic and the given output estimates are just examplars.

**An example of a printed output data is given below:**

```
Age-sex-adjusted prevalence for ['asthma'] is 1300.0 per 10,000 ( 1171.1 , 2771.1 )
Age-sex-adjusted prevalence for ['diabetes '] is 1850.0 per 10,000 ( 228.4 , 3471.6 )
Age-sex-adjusted prevalence for ['hypertension'] is 3150.0 per 10,000 ( 967.2 , 5332.8 )
Age-sex-adjusted prevalence for ['depression'] is 2450.0 per 10,000 ( 489.6 , 4410.4 )
```


**An example of a written text file is given below:**

| disease | Age-sex-adjusted prevalence | CI | 
| ------------- | ------------- | ------------
| asthma | 1300.0 | 1171.1 , 2771.1 
| diabetes	| 1850.0 | 228.4 , 3471.6 
| hypertension | 3150.0 | 967.2 , 5332.8
| depression	| 2450.0 | 489.6 , 4410.4

