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
plt.figure(figsize=(12, 6))
plt.plot(df['Tanggal'], df['Harga Saham'], color='green', marker='*', linestyle='-', label= 'harga saham')
