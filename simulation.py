#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from particle import Particle


def simulate(j):
    xs = []
    ys = []
    cs = []

    deltaT = DT # Possible implementation of a variable timestep
    
    for i in particles:
        i.integratePosVel(deltaT, particles)

        xs.append(i.pos[0])
        ys.append(i.pos[1])
        cs.append(i.color)
    #print(f'\rStep {j} ended.', end='', flush=True)
    print(f'\r{cs}', end='', flush=True)

    ax1.clear()

    ax1.scatter(xs, ys, s=2, c=cs[:])

    #ax1.set_xlabel('X Position (AU)')
    #ax1.set_ylabel('Y Position (AU)')
    ax1.set_axis_off()

    plt.xlim(-BOUNDS, BOUNDS)
    plt.ylim(-BOUNDS, BOUNDS)


IC_FILE = 'ICexamples/dataPlanets.txt' # initial conditions file
COLOR_FILE = 'ICexamples/colorPlanets.txt'
CONST_G = 4 * np.pi**2
DT = 1e-2 # Integration time step
BOUNDS = 30 # Graph bounds (AU)
ITVL_PYPLOT = 50 # Interval of each step in the animation (miliseconds)

# Configuring figure

plt.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "black",
    "axes.facecolor": "white",
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "savefig.edgecolor": "black"})

fig = plt.figure()
ax1 = plt.axes(xlim=(-BOUNDS, BOUNDS), ylim=(-BOUNDS, BOUNDS))
ax1.set_aspect('equal')


# Reading initial conditions
m, px, py, pz, vx, vy, vz = np.loadtxt(IC_FILE, unpack=True)

cs = []
try:
    cs = np.loadtxt(COLOR_FILE, unpack=True, dtype='str', comments='%')
    print(f'Colors read: {cs}')
except OSError:
    print('Color file was not found or it doesn\'t exist.')


# Defining particles
particles = []
if len(cs) == len(m):
    for cm, cpx, cpy, cpz, cvx, cvy, cvz, cc\
        in zip(m, px, py, pz, vx, vy, vz, cs):

        p = [cpx, cpy, cpz]
        v = [cvx, cvy, cvz]
        c = cc

        particles.append(Particle(cm, p, v, c=cc))

else:
    for cm, cpx, cpy, cpz, cvx, cvy, cvz\
        in zip(m, px, py, pz, vx, vy, vz):
        
        p = [cpx, cpy, cpz]
        v = [cvx, cvy, cvz]

        particles.append(Particle(cm, p, v))
    

anim = animation.FuncAnimation(fig,
                                simulate,
                                interval=ITVL_PYPLOT,
                                blit=False)
# aparently, if the interval is too small for a certain amount of data, the
# graph is not plotted.

plt.show()
