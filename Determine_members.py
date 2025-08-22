import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

file_path = r"C:\Users\gun53\Downloads\M06-result.csv"
data = pd.read_csv(file_path)

data_filtered = data.dropna(subset=['pmra', 'pmdec'])

center_pmra = -2.8
center_pmdec = -5.6
radius = 2.5

distance = ((data_filtered['pmra'] - center_pmra)**2 + (data_filtered['pmdec'] - center_pmdec)**2)**0.5
data_in_circle = data_filtered[distance <= radius]

output_file_path = r"C:\Users\gun53\Downloads\data_2d_M77.csv"
data_in_circle.to_csv(output_file_path, index=False)

plt.figure(figsize=(8, 6))
plt.scatter(data_filtered['pmra'], data_filtered['pmdec'], alpha=0.7, c='blue', s=5)

circle = patches.Circle((center_pmra, center_pmdec), radius=radius, edgecolor='red', facecolor='none', lw=2)
plt.gca().add_patch(circle)

plt.title('Proper Motion (pmra vs pmdec)')
plt.xlabel('pmra (mas/year)')
plt.ylabel('pmdec (mas/year)')

plt.xlim(-20, 10)
plt.ylim(-10, 10)

plt.grid(True)

plt.show()
