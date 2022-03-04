#Creates a disk centralized at centerPos in plane xy

import numpy as np
from particle import particle

outputFile = 'ic2.txt'

bodies = 10
constG = 4*np.pi**2

centerPos = 0.0
stdDevPos = 30.0

centerMass = 5.0
stdDevMass = 1.0


#Generating a gaussian distribution of masses and positions
randomXs = np.random.normal(centerPos, stdDevPos, bodies)
randomYs = np.random.normal(centerPos, stdDevPos, bodies)
randomMs = np.random.normal(centerMass, stdDevMass, bodies)

particles = []

for i in range(bodies):
    a = particle()
    a.setInitialConditions(randomMs[i], [randomXs[i], randomYs[i], 0.0], [0.0, 0.0, 0.0])

    particles.append(a)


#Calculating totalMass
totalMass = 0.0

for i in particles:
    totalMass += i.mass


#Calculating center of mass
centerOfMass = np.zeros(3)
for i in particles:
    centerOfMass = i.mass * i.pos
centerOfMass = centerOfMass / totalMass


#Calculating distances to center of mass
distancesCM = []
for i in range(bodies):
    distancesCM.append(np.linalg.norm(particles[i].pos - centerOfMass))


#Calculating velocity norm, considering a circular motion
velocities = []
for i in range(bodies):
    
    innerMass = 0.0
    for k in range(bodies):
        if i != k:
            innerMass += particles[k].mass
    
    velocities.append(np.sqrt(constG * innerMass / distancesCM[i]))


#Calculating angles and setting velocity vectors
angles = []
for i in particles:
    c = complex(i.pos[0], i.pos[1])
    angles.append(np.angle(c))

for i in range(bodies):

    v = [velocities[i] * np.cos(angles[i] + np.pi/2), velocities[i] * np.sin(angles[i] + np.pi/2), 0.0]

    particles[i].setInitialConditions(randomMs[i], [randomXs[i], randomYs[i], 0.0], v)


#Organizing data to be saved
data = []

for i in particles:
    data.append([i.mass, i.pos[0], i.pos[1], i.pos[2], i.vel[0], i.vel[1], i.vel[2]])


np.savetxt(outputFile, data, header='m      px      py      pz      vx      vy       vz')
