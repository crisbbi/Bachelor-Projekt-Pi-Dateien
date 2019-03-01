from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import IMU
""""
fig = plt.figure()
ax = fig.gca(projection='3d')

# Make the grid
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))

# Make the direction data for the arrows
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))

ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)

plt.show()
"""
fig = plt.figure()
ax = fig.gca(projection='3d')


Q = ax.quiver(0, 0, 0, 0, 0, 0, length=0.1, normalize=True)

def animate(Q):
    r_x = IMU.readGYRx()
    r_y = IMU.readGYRy()
    r_z = IMU.readGYRz()

    r_x_matrix = np.array([[1, 0, 0],
                           [0, np.cos(np.rad2deg(r_x)), -np.sin(np.rad2deg(r_x))],
                           [0, np.sin(np.rad2deg(r_x)), np.cos(np.rad2deg(r_x))]])

    r_y_matrix = np.array([[np.cos(np.rad2deg(r_y)), 0, np.sin(np.rad2deg(r_y))],
                           [0, 1, 0],
                           [-np.sin(np.rad2deg(r_y)), 0, np.cos(np.rad2deg(r_y))]
                           ])
    r_z_matrix = np.array([[np.cos(np.rad2deg(r_z)), -np.sin(np.rad2deg(r_z)), 0],
                          [np.sin(np.rad2deg(r_z)), np.cos(np.rad2deg(r_z)), 0],
                          [0, 0, 1]])
    r_xy = np.matmul(r_x_matrix, r_y_matrix)
    r_xyz = np.matmul(r_xy, r_z_matrix)
    e_x = np.matmul(r_xyz, [1, 0, 0])
    e_y = np.matmul(r_xyz, [0, 1, 0])
    e_z = np.matmul(r_xyz, [0, 0, 1])
    print("X: %i, Y: %i , Z: %i" %(r_x,r_y,r_z))
    ax.clear()

    return ax.quiver(0, 0, 0, e_x, e_y, e_z, length=0.1, normalize=True)



ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()
