import numpy as np
import matplotlib.pyplot as plt

# Simuler tidspunkter (dage)
time = np.linspace(0, 10, 100)

# Simuler plasmaniveauer for intravenøs administration (hurtig stigning og fald)
iv_levels = 100 * np.exp(-0.5 * time)

# Simuler plasmaniveauer for subkutan administration (langsom stigning og fald)
sc_levels = 50 * (1 - np.exp(-0.5 * time))

plt.figure(figsize=(10, 6))
plt.plot(time, iv_levels, label='Intravenøs Administration')
plt.plot(time, sc_levels, label='Subkutan Administration')
plt.xlabel('Tid (dage)')
plt.ylabel('Plasmaniveau (arbitære enheder)')
plt.title('Simulerede Plasmaniveauer: Intravenøs vs Subkutan Administration')
plt.legend()
plt.grid(True)
plt.show()
