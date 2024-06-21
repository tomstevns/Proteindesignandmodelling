# Generer hypotetiske data for behandlingsresultater
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
treatments = ['Epcoritamab', 'Mosunetuzumab', 'Glofitamab']
data = {
    'PatientID': range(1, 101),
    'Treatment': np.random.choice(treatments, 100),
    'Response': np.random.choice(['CR', 'PR', 'SD', 'PD'], 100, p=[0.3, 0.4, 0.2, 0.1]),  # CR = Complete Response, PR = Partial Response, SD = Stable Disease, PD = Progressive Disease
    'CRS_Severity': np.random.choice(['None', 'Mild', 'Moderate', 'Severe'], 100, p=[0.5, 0.3, 0.15, 0.05])
}

df_treatment = pd.DataFrame(data)

# Visualiser behandlingsresultater og CRS-severitet
plt.figure(figsize=(12, 8))
sns.countplot(x='Treatment', hue='Response', data=df_treatment)
plt.xlabel('Behandling')
plt.ylabel('Antal')
plt.title('Behandlingsresultater pr. Behandlingstype')
plt.legend(title='Respons')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 8))
sns.countplot(x='Treatment', hue='CRS_Severity', data=df_treatment)
plt.xlabel('Behandling')
plt.ylabel('Antal')
plt.title('CRS Severity pr. Behandlingstype')
plt.legend(title='CRS Severity')
plt.grid(True)
plt.show()
