import numpy as np

constG = 4 * np.pi**2


class particle ():
    mass = 0.0
    pos = np.array([0.0, 0.0, 0.0])
    vel = np.array([0.0, 0.0, 0.0])
    acel = np.array([0.0, 0.0, 0.0])


    def setInitialConditions (self, m, r, v):
        self.mass = m
        self.pos = np.array(r)
        self.vel = np.array(v)
        self.acel = np.array([0.0, 0.0, 0.0])

    
    def getAcel (self, position, particles):
        #Returns the aceleration for an input position of the particle
        acel = np.array([0.0,0.0,0.0])
        for i in particles:
            if self != i:
                acel = (constG * i.mass\
                    / (np.linalg.norm(i.pos - position) ** 3))\
                    * (i.pos - position) + acel
            else:
                pass

        return (acel)


    def integratePosVel (self, deltaT, particles):
        #utilizing the leapfrog method
        velHalf = self.vel + self.acel * deltaT / 2
        self.pos = self.pos + velHalf * deltaT
        self.acel = self.getAcel(self.pos, particles)
        self.vel = velHalf + self.acel * deltaT / 2


def prepareData (particles, particleNumber):
    pos = []
    vel = []
    mass = []
    for i in particles:
        for j in range(3): # for the 3 dimensions of positions and velocities
            pos.append(i.pos[j])
            vel.append(i.pos[j])
        mass.append(i.mass)
        return([pos, vel, range(particleNumber), mass])
