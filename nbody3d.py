 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import time

PARTICLES_LIMIT = 50
STEPS_LIMIT = 100
DIMENSIONS = [i for i in range(3)]
STEP_SIZE = 0.001
TIME = 1

class Particle:
    index = 1
    postion = DIMENSIONS
    speed = DIMENSIONS
    force = DIMENSIONS
    force_old = DIMENSIONS
    mass = 0

    def __init__(self, index) -> None:
        self.index = index
        # Генеруємо випадкову позицію
        self.postion = [np.random.uniform(0, 1) for _ in DIMENSIONS]
        # Генеруємо випадкову швидкість
        self.velocity = [np.random.uniform(-1, 1) for _ in DIMENSIONS]
        # Початкова сила
        self.force = [0 for _ in DIMENSIONS]
        self.force_old = self.force
        # Масса
        self.mass = np.random.uniform(0, 0.7)
        # Генеруємо випадковий RGB колір
        self.color = tuple((np.random.uniform(0, 1) for _ in range(3)))

    def clear_force(self):
        self.force = [0 for _ in DIMENSIONS]

    def update_position(self):
        a = STEP_SIZE * 0.5 / self.mass
        for dimension in DIMENSIONS:
            self.postion[dimension] += STEP_SIZE * (
                self.velocity[dimension] + a * self.force[dimension]
            )
        self.force_old[dimension] = self.force[dimension]
        #print(self.postion)

    def update_velocity(self):
        a = STEP_SIZE * 0.5 / self.mass
        for dimension in DIMENSIONS:
            self.velocity[dimension] += a * (
                self.force[dimension] + self.force_old[dimension]
            )


class Nbody:
    particles = []

    def __init__(self, particles) -> None:
        self.particles = particles
        self.update_forces()
    
    def clear_forces(self):
        for particle in self.particles:
            particle.clear_force()

    def update(self):
        self.update_forces()
        self.update_positions()
        self.update_velocities()

    def update_forces(self):
        self.clear_forces()
        for aParticle in self.particles:
            for bParticle in self.particles:
                if aParticle.index == bParticle.index:
                    continue
                Nbody.__update_force(aParticle, bParticle)

    def update_positions(self):
        for particle in self.particles:
            particle.update_position()

    def update_velocities(self):
        for particle in self.particles:
            particle.update_velocity()

    @staticmethod
    def __calculateForce(aPosition, aMass, bPosition, bMass, DIMENSIONS):
        r = np.float64(1e-4)
        # G = 6.67430e-11
        G = 10
        for dimension in DIMENSIONS:
            r += np.square(bPosition[dimension] - aPosition[dimension])
        force = G * aMass * bMass / (np.sqrt(r) * r)
        result = []
        for dimension in DIMENSIONS:
            result.append(force * (bPosition[dimension] - aPosition[dimension]))
        return result

    @staticmethod
    def __update_force(aParticle: Particle, bParticle: Particle):
        aPosition = aParticle.postion
        bPosition = bParticle.postion
        force = Nbody.__calculateForce(
            aPosition, aParticle.mass, bPosition, bParticle.mass, DIMENSIONS
        )
        for dimension in DIMENSIONS:
            aParticle.force[dimension] += force[dimension]
            bParticle.force[dimension] -= force[dimension]

    def set_scatter(self, ax):
        x = []
        y = []
        z = []
        sizes = []
        colors = []
        for particle in self.particles:
            x.append(particle.postion[0])
            y.append(particle.postion[1])
            z.append(particle.postion[2])
            sizes.append(np.square(particle.mass * 10) + 20)
            colors.append(particle.color)
        ax.scatter(x, y, z, s=sizes, c=colors)



def generate_particles(limit):
    for i in range(1, limit + 1):
        yield Particle(i)


def init():
    particles_gen = generate_particles(PARTICLES_LIMIT)
    particles = []
    for particle in particles_gen:
        # print(particle.postion)
        particles.append(particle)
    nbody = Nbody(particles)
    plt.style.use('_mpl-gallery')
    # values on x-axis
    x = [0, 0.3, 0.5, 0.7, 1]
    # values on y-axis
    y = [0, 0.3, 0.5, 0.7, 1]
    z = [0, 0.3, 0.5, 0.7, 1]
    fig, ax = plt.subplots(figsize=(10,10))
    fig.tight_layout()
    ax = plt.axes(projection='3d')
    ax.set(xlim=(0, 1), ylim=(0, 1), zlim=(0,1), xticks=np.arange(0, 1), yticks=np.arange(0, 1),zticks=np.arange(0, 1))
    ax.set_aspect('auto', 'box')
    for time in range(STEPS_LIMIT):
        plt.cla()
        ax.set_xlim((0, 1))
        ax.set_ylim((0, 1))
        ax.set_zlim((0, 1))
        nbody.update()
        nbody.set_scatter(ax)
        plt.pause(0.05)
        #plt.savefig('nbody3d/' + str(time) + 'body.png')

    plt.close()

if __name__ == "__main__":
    time1 = time.perf_counter()
    init()

#Лічильник
time2=time.perf_counter()
time0=time2-time1
print("It took me", round(time0, 2), "seconds")