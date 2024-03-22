import pandas as pd

file_path_concatenado = 'Data_created/df_concatenado.csv'
# file_path_covid_combined = 'Data_created/df_covid_combined.csv'

file_path_covid_combined = 'Data_created/df_covid_comb_all.csv'


df_concatenado = pd.read_csv(file_path_concatenado)
df_covid_combined = pd.read_csv(file_path_covid_combined)



news_names_concatenado = {'trade': 'Trade (% GDP)', 'poorest_decile_threshold': 'Poorest decile threshold',
                            'GINI':'Gini Coefficient', 'median_income':'Median income', 'richest_decile_threshold':'Richest decile threshold',
                            'Education':'Money spent in the education area'}

df_concatenado = df_concatenado.rename(columns=news_names_concatenado)

news_names_covid = {'total_deaths': 'Total Deaths', 'total_cases_per_million': 'Total cases per million',
                            'new_cases_smoothed_per_million':'New cases per million', 'stringency_index':'Stringency index', 
                            'weekly_hosp_admissions_per_million':'Weekly hospitalizations per million',
                            'HICP':'Inflation rate'}

df_covid_combined = df_covid_combined.rename(columns=news_names_covid)
