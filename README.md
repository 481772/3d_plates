# 3D printing the Earth's tectonic plates

This project aims to convert the Earth's tectonic plates into 3d-printed models. We adopt [Peter Bird's plate models](https://doi.org/10.1029/2001GC000252) and the plate polygons available in [https://github.com/fraxen/tectonicplates](https://github.com/fraxen/tectonicplates).

- step 1: `3d_plate.py` turns longitude and latitude coordinates of [the point set forming plate polygons](https://github.com/fraxen/tectonicplates/blob/master/original/PB2002_plates.dig.txt) into cartesian coordinates (x, y, z):

$$
\begin{split}
\theta &= \frac{\pi}{180}(90^{\circ}-\text{lat}^{\circ}) \\
\phi   &= \frac{\pi}{180}\text{lon}^{\circ} \textrm{ if lon}^{\circ} \ge 0^{\circ}, \quad \frac{\pi}{180}(180^{\circ}-\text{lon}^{\circ}) \textrm{ if lon}^{\circ} < 0^{\circ} \\
x &= r\sin\theta\cos\phi \\
y &= r\sin\theta\sin\phi \\
z &= r\cos\theta,
\end{split}
$$

where $r$ is the radius of an assumed sphere (e.g., 10 cm).
