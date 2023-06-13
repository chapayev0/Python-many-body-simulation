import numpy as np
import matplotlib.pyplot as plt

# Constants (values are in astronomical units, masses in solar masses, and time in years)
G = 39.478  # Gravitational constant
dt = 0.001  # Time step

# Define the initial conditions (positions, velocities, masses) for the Sun and the planets
positions = np.array([[0, 0, 0],  # Sun
                      [0.387, 0, 0],  # Mercury
                      [0.723, 0, 0],  # Venus
                      [1.0, 0, 0],  # Earth
                      [1.524, 0, 0],  # Mars
                      [5.203, 0, 0],  # Jupiter
                      [9.539, 0, 0],  # Saturn
                      [19.18, 0, 0],  # Uranus
                      [30.07, 0, 0]])  # Neptune

velocities = np.array([[0, 0, 0],  # Sun
                       [0, 12.44, 0],  # Mercury
                       [0, 10.36, 0],  # Venus
                       [0, 9.0, 0],  # Earth
                       [0, 7.64, 0],  # Mars
                       [0, 5.43, 0],  # Jupiter
                       [0, 4.29, 0],  # Saturn
                       [0, 3.02, 0],  # Uranus
                       [0, 2.48, 0]])  # Neptune

masses = np.array([1.0,  # Sun
                   1.66e-7,  # Mercury
                   2.45e-6,  # Venus
                   3.0e-6,  # Earth
                   3.22e-7,  # Mars
                   9.55e-4,  # Jupiter
                   2.85e-4,  # Saturn
                   4.36e-5,  # Uranus
                   5.18e-5])  # Neptune

# Number of bodies
num_bodies = len(positions)

# Array to store the positions over time
trajectory = np.zeros((num_bodies, 3, int(10 / dt)))  # Adjust the duration if necessary

# Perform the simulation
for t in range(int(10 / dt)):
    # Compute the pairwise distances between bodies
    distances = positions[:, np.newaxis, :] - positions[np.newaxis, :, :]
    # Compute the magnitudes of the distances
    magnitudes = np.linalg.norm(distances, axis=2)
    # Avoid division by zero
    np.fill_diagonal(magnitudes, 1)
    # Compute the gravitational forces between bodies
    forces = G * (masses[:, np.newaxis] * masses[np.newaxis, :] / magnitudes**3) * distances
    # Sum up the forces acting on each body
    total_forces = np.sum(forces, axis=1)
    # Compute the accelerations
    accelerations = total_forces / masses[:, np.newaxis]
    # Update the velocities and positions using the Verlet algorithm
    positions += velocities * dt + 0.5 * accelerations * dt**2
    velocities += 0.5 * accelerations * dt
    # Store the positions in the trajectory array
    trajectory[:, :, t] = positions

# Plotting the trajectories
for i in range(num_bodies):
    plt.plot(trajectory[i, 0, :], trajectory[i, 1, :])
plt.title("Solar System Simulation")
plt.xlabel("X position (AU)")
plt.ylabel("Y position (AU)")
plt.show()
