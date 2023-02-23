# nbody-py
This is my second-year university project on n-body problem.

For correct work of program you need such libraries:
matplotlib
numpy
time

File description:
nbody2d.py - program set up for 2-dimension case
nbody3d.py - program set up for 3-dimension case.

Description of some adjustable lines:
7 PARTICLES_LIMIT = 1000 — you can set number of bodies(particles)

8 STEPS_LIMIT = 100 — you can set number of calculations steps
9 DIMENSIONS = [i for i in range(2)] — number of dimensions
10 STEP_SIZE = 0.001 — size of a step

After uncommenting line
152/158 #plt.savefig('nbody/' + str(time) + 'body.png')
and after making folder named "nbody" in file containing folder, you can get .png images of each step.

Also you can give bodies different mass, starting position, speed and interaction force, which is commented in the code.
