import numpy as np
from marching_cubes import MarchingCubes
import matplotlib.pyplot as plt
from itertools import product, combinations
from skimage.draw import ellipsoid
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure(figsize=(15, 10))
ax = plt.axes(projection="3d")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
r = [0, 50]
arr = ellipsoid(20, 20, 20)
for s, e in combinations(np.array(list(product(r, r, r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s, e), color="#FFFFFF00")

ax.add_collection3d(Poly3DCollection(MarchingCubes.marching_cubes(arr, 2), edgecolors="red", facecolors="#FFFFFF00"))
plt.show()




