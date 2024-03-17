import pandas as pd

file_path_concatenado = 'Data_created/df_concatenado.csv'
file_path_covid_combined = 'Data_created/df_covid_combined.csv'

df_concatenado = pd.read_csv(file_path_concatenado)
df_covid_combined = pd.read_csv(file_path_covid_combined)
