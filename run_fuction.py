# import libraries:
import pandas as pd
import numpy as np

# import the function by loading the module (calc_adjust_rate.py)
import calc_adjust_rate


# Load data
participants = pd.read_csv("data/participants.txt", sep='\t')
diseases = pd.read_csv("data/diseases.txt", sep='\t')
census = pd.read_csv("data/english_census_2021.txt", sep='\t')

# Calculate the adjusted rates
calc_adjust_rate.age_sex(participants, diseases, census, pd, np, popsize = 10000)
