import numpy as np

constG = 4 * np.pi**2


class Particle():

    def __init__ (self, m, r, v, c='#1f77b4'):
        self.mass = m
        self.pos = np.array(r)
        self.vel = np.array(v)
        self.acel = np.array([0.0, 0.0, 0.0])
        self.color = c

    
    def _getAcel(self, position, particles):
        acel = np.array([0.0,0.0,0.0])
        for i in particles:
            if self != i:
                acel = (constG * i.mass\
                    / (np.linalg.norm(i.pos - position) ** 3))\
                    * (i.pos - position) + acel
            else:
                pass

        return acel


    def integratePosVel(self, deltaT, particles):
        # utilizing the leapfrog method
        velHalf = self.vel + self.acel * deltaT / 2
        self.pos = self.pos + velHalf * deltaT
        self.acel = self._getAcel(self.pos, particles)
        self.vel = velHalf + self.acel * deltaT / 2


def prepareData (particles, particleNumber):
    """
    This function takes a list of particle objects and prepares all relevant
    data to be written in Gadget format.

    Not used in this version.
    """

    pos = []
    vel = []
    mass = []
    for i in particles:
        for j in range(3): # for the 3 dimensions of positions and velocities
            pos.append(i.pos[j])
            vel.append(i.pos[j])
        mass.append(i.mass)
        return [pos, vel, range(particleNumber), mass]
