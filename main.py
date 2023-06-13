# -*- coding: utf-8 -*-

import sys
import platform
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

from ui.ui_main import *

global_state = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        def move_window(event):

            if event.buttons() == Qt.LeftButton:

                self.move(self.pos() + event.globalPos() - self.dragpos)
                self.dragpos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = move_window

        #button comands
        self.ui.close_btn.clicked.connect(self.terminate_fun)
        self.ui.maxmize_btn.clicked.connect(self.maxmize_fun)
        self.ui.minimize_btn.clicked.connect(self.minimize_fun)
        self.ui.home_btn.clicked.connect(self.plot_show)

    def plot_test(self):

        fig = Figure(figsize=(7, 5), dpi=65, facecolor=(1, 1, 1), edgecolor=(0, 0, 0))
        self.canvas = FigureCanvas(fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.lay = QVBoxLayout()
        self.lay.addWidget(self.toolbar)
        self.lay.addWidget(self.canvas)
        self.ui.plot_screen.setLayout(self.lay)

    def plot_show(self):

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

        # Celestial body labels
        labels = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

        # Number of bodies
        num_bodies = len(positions)

        # Array to store the positions over time
        trajectory = np.zeros((num_bodies, int(10 / dt), 3))  # Adjust the duration if necessary

        # Perform the simulation
        for t in range(int(10 / dt)):
            # Compute the pairwise distances between bodies
            differences = positions[:, np.newaxis, :] - positions[np.newaxis, :, :]
            distances = np.linalg.norm(differences, axis=2)
            # Avoid division by zero
            np.fill_diagonal(distances, 1)
            # Compute the gravitational forces between bodies
            forces = G * (masses[:, np.newaxis] * masses[np.newaxis, :] / distances ** 3)[:, :,
                         np.newaxis] * differences
            # Sum up the forces acting on each body
            total_forces = np.sum(forces, axis=1)
            # Compute the accelerations
            accelerations = total_forces / masses[:, np.newaxis]
            # Update the velocities and positions using the Verlet algorithm
            positions += velocities * dt + 0.5 * accelerations * dt ** 2
            velocities += 0.5 * accelerations * dt
            # Store the positions in the trajectory array
            trajectory[:, t, :] = positions

        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the trajectory as elliptical paths and add a legend
        for i in range(num_bodies):
            ax.plot(trajectory[i, :, 0], trajectory[i, :, 1], trajectory[i, :, 2], label=labels[i])

            # Plot the last position as a circular marker
            ax.scatter(trajectory[i, -1, 0], trajectory[i, -1, 1], trajectory[i, -1, 2], s=10, color='black')

        # Set labels and title
        ax.set_xlabel('X position (AU)')
        ax.set_ylabel('Y position (AU)')
        ax.set_zlabel('Z position (AU)')
        ax.set_title('Solar System Simulation')

        ax.spines['top'].set_visible(True)
        ax.spines['right'].set_visible(True)
        ax.spines['bottom'].set_visible(True)
        ax.spines['left'].set_visible(True)

        # Add a legend in the top right corner
        ax.legend(loc='best')

        # Show the plot
        #plt.show()

        self.canvas = FigureCanvas(fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.lay = QVBoxLayout()
        self.lay.addWidget(self.toolbar)
        self.lay.addWidget(self.canvas)
        self.ui.plot_screen.setLayout(self.lay)
        self.canvas



    def mousePressEvent(self, event):

        self.dragpos = event.globalPos()

    def maxmize_fun(self):

        global global_state

        status = global_state

        if status == 0:

            self.showMaximized()
            global_state = 1


        else:

            global_state = 0
            self.showNormal()



    def terminate_fun(self):

        self.close()

    def minimize_fun(self):

        global global_state
        self.showMinimized()


    def return_status_max(self):

        global global_state

        return global_state



if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
