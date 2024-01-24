import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membuat data sintetis
tanggal = pd.date_range(start="2023-01-01", end="2023-09-03", freq='D')
harga_saham = np.random.randn(len(tanggal)).cumsum() + 50 #random walk

df = pd.DataFrame({
    'Tanggal': tanggal,
    'Harga Saham': harga_saham
})

# Membuat line plot
plt.figure(figsize=(12, 6))
plt.plot (df['Tanggal'], df['Harga Saham'], color='blue', label='Harga Saham')
plt.title('Perubahan Harga Saham Selama Tahun 2023')
plt.xlabel('Tanggal')
plt.ylabel('Harga Saham')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()