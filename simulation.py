import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from particle import particle


icFile = 'ICexamples/dataPlanets.txt' # initial conditions file

constG = 4 * np.pi**2
dt = 1e-2 # Integration time step

bounds = 75 # Graph bounds (AU)

itvlPyplot = 50 # Interval of each step in the animation (miliseconds)


m, px, py, pz, vx, vy, vz = np.loadtxt(icFile, unpack=True)

particles = []
for i in range(len(m)):
    a = particle()

    p = [px[i], py[i], pz[i]]
    v = [vx[i], vy[i], vz[i]]

    a.setInitialConditions(m[i], p, v)
    
    particles.append(a)


# Configuring figure
plt.style.use('dark_background')
fig = plt.figure()
ax1 = plt.axes(xlim=(-bounds, bounds), ylim=(-bounds, bounds))
ax1.set_aspect('equal')


def simulate(j):
    xs = []
    ys = []

    deltaT = dt # Possible implementation of a variable timestep
    
    for i in particles:
        i.integratePosVel(deltaT, particles)

        xs.append(i.pos[0])
        ys.append(i.pos[1])
    print(f'Step {j} ended.')

    ax1.clear()

    ax1.scatter(xs, ys)

    ax1.set_xlabel('X Position (AU)')
    ax1.set_ylabel('Y Position (AU)')

    plt.xlim(-bounds, bounds)
    plt.ylim(-bounds, bounds)
    

anim = animation.FuncAnimation(fig,
                                simulate,
                                interval=itvlPyplot,
                                blit=False)
# aparently, if the interval is too small for a certain amount of data, the
# graph is not plotted.

plt.show()
