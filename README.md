# particleSim

Simple python script that simulates gravity through direct sum.

This version uses natural units where the gravitational constant is
<img src="https://render.githubusercontent.com/render/math?math=4 \pi^2">.

Example dataPlanets.txt uses real data (that can be verified in
 ICexamples/data) and normalizes positions, velocities and mass to make a
 solar system simulation.


# Usage

Currently, the code needs to have configured manually all plot parameters,
which means that most customization is done in the code itself rather than
using argparser or other tool.

It should work out-of-the-box just by executing `python3 simulation.py`.

This code also makes use of [Numpy](https://numpy.org/), which can be
installed with `python3 -m pip install numpy`.


# Initial Conditions

Initial conditions are read by `numpy.loadtxt()` as a text file written as a
matrix, where each line corresponds to a particle and the columns must be in
the order `m x y z vx vy vz`, where `m` stands for mass, `x y z` correlates to
cartesian coordinates and `vx vy vz` are the cartesian velocities.
