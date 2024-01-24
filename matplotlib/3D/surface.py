from mpl_toolkits.mplot3d import Axes3D

# membuat data untuk 3D plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid (x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# membuat 3D wiraframe plot
fig = plt.figure (figsize=(10, 8))
ax = fig.add_subplot (111, projection='3d')
surf = ax.plot_surface( X, Y, Z, cmap='viridis')

# menambahakna color bar
fig.colorbar (surf, shrink=0.5, aspect=10)
# menambahkan judul dan label 
ax.set_title('3D Wireframe Plot dari Fungsi z = sin(sqrt(x^2 + y^2)) ')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show ()