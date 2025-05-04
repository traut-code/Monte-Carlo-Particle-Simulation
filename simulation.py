import numpy as np
import matplotlib.pyplot as plt

#Parameters 
initial_energy = 100
step_size = 1
num_particles = 100

ranges = []

for _ in range(num_particles):
	position += step_size
	energy = initial_energy

	while energy >0:
		position += step_size
		energy_loss = np.random.uniform(1, 5)
		energy -= energy_loss
	
	ranges.append(position)

plt.hist(ranges, bins=15, edgecolor='black')
plt.title('Particel Penetration Range Distribution')
plt.xlabel('Range (Distance Travelled)')
plt.ylabel('Number of Particles')
plt.grid(true)
plt.show()

