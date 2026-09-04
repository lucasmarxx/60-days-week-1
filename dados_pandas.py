import pandas as pd
import numpy as np
import kagglehub

# Dataset do kagglehub sobre a EWC 2026
# path = kagglehub.dataset_download('maulikgajera/esports-world-cup-2026-dataset')
# print('path:', path)

df = pd.read_csv('01_EWC2026_Event_Tournament_Summary.csv')

# print(df.info())
# print(df.describe())
# print(df.head(2))
filtro_vice = df['Runner_Up']
vencedor_e_premio = df[['Prize_Pool_USD', 'Winner']]

filtro_1 = df[df['Gender'] == "Women's"]
filtro_2 = df[df['Prize_Pool_USD'] > 500000]
filtro_3 = df[df['Platform'] == 'Mobile']
filtro_4 = df[df['Game_Type'] == 'MOBA']

print(f'{filtro_1}\n{"-" * 200}')
print(f'{filtro_2}\n{"-" * 200}')
print(f'{filtro_3}\n{"-" * 200}')
print(f'{filtro_4}\n{"-" * 200}')