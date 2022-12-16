# build the function
def age_sex(participants, diseases, census, pd, np, popsize = 10000):
    '''
    Function to calculate age and sex adjusted prevelance for one or more diseases

    Input are three pandas dataframes:
    
    participant: should include sample id, gender and age_group
    disease: should specify the sample id and disease of affected individuals
    cencus: should give the precentage distribution by age and gender from a standard population
    popsize: default is 10.000 but this can be any number depending on how you want to express the rate
    '''

    # Define lists
    all_diseases = diseases['disease'].unique()
    disease_list = []
    prev_list = []
    ci_list = []
    df = pd.DataFrame()
    
    # get the participant IDs and demographic info of interest for each disease:
    for i in all_diseases:
        disease_participant = diseases.loc[(diseases['disease'] == i) & (diseases['participant_id'].isin(participants.participant_id))]
        demo_participant = participants.loc[participants['participant_id'].isin(disease_participant.participant_id)]

        ## prepare data for age-and-sex-adjusted prevalence calculations:
        # get counts "freq_x" of participants for each condition in each age group by gender
        disease_count_age_sex = demo_participant.groupby(['age_group', 'sex'])['sex'].size().reset_index(name='freq_x')
        
        # get counts "freq_y"of population in for each condition in each age group by gender
        population_count_age_sex = participants.groupby(['age_group', 'sex'])['sex'].size().reset_index(name='freq_y')
        
        # merge the two datasets to calculate age and sex specific rate
        age_sex_adjusted_rate = pd.merge(population_count_age_sex, disease_count_age_sex,
                                        on = ["age_group",'sex'] , how= "left")

        # merge census data with the above datasets to calculate "weighted" age and sex specific rate
        age_sex_adjusted_rate = pd.merge(age_sex_adjusted_rate, census,
                                         on = ["age_group",'sex'] , how= "left")

        ## age-and-sex-adjusted prevalence calculations:
        # calculate age and sex specific rate "crude rate"; by popsize
        age_sex_adjusted_rate['age_sex_specific_rate']= round(age_sex_adjusted_rate['freq_x']
                                                              /age_sex_adjusted_rate['freq_y'] * popsize, 2)

        # calculate weighted age and sex specific_rate
        # multiply the specific rates by percentage of standard population found in census data
        age_sex_adjusted_rate['weighted_age_specific_rate']= round(age_sex_adjusted_rate['age_sex_specific_rate']
                                                                   *age_sex_adjusted_rate['percentage'], 2)

        # sum weighted age and sex specific rates
        # the total of these rates is the age-sex adjusted rate for this particular community
        age_sex_adjusted_rate.loc['Total']= age_sex_adjusted_rate.sum(numeric_only=True, axis=0).round(2)

        ## calculate 95% confidence interval for each adjusted prevalence 
        R = age_sex_adjusted_rate.loc['Total','weighted_age_specific_rate']
        N = diseases.loc[(diseases['disease'] == i) & 
                         (diseases['participant_id'].isin(participants.participant_id))]['participant_id'].count().astype(float)
        SE = R/np.sqrt(N)
        CI_plus = R + (1.96*SE).round(1)
        CI_minus = R - (1.96*SE).round(1)
            
        # record findings for all diseases:
        print(f"Age-sex-adjusted prevalence for {disease_participant['disease'].unique()} is {age_sex_adjusted_rate.loc['Total','weighted_age_specific_rate']} per {popsize} (95% CI [{round(CI_minus,2)}, {round(CI_plus,2)}])")
        disease_list.append(i)
        prev_list.append(age_sex_adjusted_rate.loc['Total','weighted_age_specific_rate'])
        ci_list.append(f"{round(CI_minus,2)} , {round(CI_plus,2)}")


    df["disease"] = disease_list
    df['Age-sex-adjusted prevalence'] = prev_list
    df['CI'] = ci_list

    # write out results:
    df.to_csv('table_age_sex_adjusted_rates.txt', index= False, sep='\t')

    
    

