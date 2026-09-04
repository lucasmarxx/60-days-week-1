import pandas as pd
import numpy as np
import kagglehub

# Dataset do kagglehub sobre a EWC 2026
# path = kagglehub.dataset_download('maulikgajera/esports-world-cup-2026-dataset')
# print('path:', path)

df = pd.read_csv('01_EWC2026_Event_Tournament_Summary.csv')

# print(df.info())
# print(df.describe())
print(df.head(2))
filtro_vice = df['Runner_Up']
vencedor_e_premio = df[['Prize_Pool_USD', 'Winner']]

print(vencedor_e_premio)