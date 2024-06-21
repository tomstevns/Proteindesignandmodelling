import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generer hypotetiske data
np.random.seed(42)
data = {
    'PatientID': range(1, 101),
    'T_cell_infiltration': np.random.normal(50, 10, 100),  # T-celle infiltration niveauer
    'Complete_Response': np.random.choice([0, 1], size=100, p=[0.7, 0.3])  # 0 = ingen CR, 1 = CR
}

df = pd.DataFrame(data)

# Visualiser sammenhængen mellem T-celle infiltration og komplet respons
plt.figure(figsize=(10, 6))
sns.boxplot(x='Complete_Response', y='T_cell_infiltration', data=df)
plt.xlabel('Komplet Respons (0 = Ingen, 1 = Ja)')
plt.ylabel('T-celle Infiltration')
plt.title('Sammenhæng mellem T-celle Infiltration og Komplet Respons')
plt.grid(True)
plt.show()
