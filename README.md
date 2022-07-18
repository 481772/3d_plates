# 3D printing the Earth's tectonic plates

This project aims to convert the Earth's tectonic plates into 3d-printed models. We adopt [Peter Bird's plate model](https://doi.org/10.1029/2001GC000252) and the derived plate polygons available in [https://github.com/fraxen/tectonicplates](https://github.com/fraxen/tectonicplates).

## Step 1: Coordinate conversion

`3d_plate.py` turns longitude and latitude coordinates of [the point set forming plate polygons](https://github.com/fraxen/tectonicplates/blob/master/original/PB2002_plates.dig.txt) (or local file, [plate_coordinates.txt](https://github.com/481772/3d_plates/blob/main/plate_coordinates.txt))  into cartesian coordinates (x, y, z):

$$
\begin{split}
\theta &= \frac{\pi}{180}(90^{\circ}-\text{lat}^{\circ}) \\
\phi   &= \frac{\pi}{180}\text{lon}^{\circ} \textrm{ if lon}^{\circ} \ge 0^{\circ}, \quad \frac{\pi}{180}(360^{\circ}+\text{lon}^{\circ}) \textrm{ if lon}^{\circ} < 0^{\circ} \\
x &= r\sin\theta\cos\phi \\
y &= r\sin\theta\sin\phi \\
z &= r\cos\theta,
\end{split}
$$

where $r$ is the radius of an assumed sphere (e.g., 10 cm).

The converted coordinates are written to files for individual plates (e.g., `AF.txt`, `AN.txt`, etc) in the directory [radian_plates](https://github.com/481772/3d_plates/tree/main/radian_plates). 

The Python code also produces a big file containing all the plate polygons' converted coordinates named `radian_plate_coords` in the same directory.
