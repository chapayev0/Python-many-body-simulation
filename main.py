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
legend_val = True
G = 39.478  # Gravitational constant
dt = 0.001

p_array = np.empty((0, 3))
v_array = np.empty((0, 3))
m_array = np.array([])
labels = []

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()

        def move_window(event):

            if event.buttons() == Qt.LeftButton:

                self.move(self.pos() + event.globalPos() - self.dragpos)
                self.dragpos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = move_window

        #self.plot_show(legend_val, G)

        #button comands
        self.ui.close_btn.clicked.connect(self.terminate_fun)
        self.ui.maxmize_btn.clicked.connect(self.maxmize_fun)
        self.ui.minimize_btn.clicked.connect(self.minimize_fun)
        self.ui.legend_chk.stateChanged.connect(self.legend_val_change)
       # self.ui.g_edit.textChanged.connect(self.g_val_change)
        self.ui.home_btn.clicked.connect(self.generate_plot)
        self.ui.set_btn.clicked.connect(self.remove_layout)
        self.ui.add_btn.clicked.connect(self.add_array_data)
        self.ui.mass_edit.returnPressed.connect(self.add_array_data)

    def clear_arrays(self):

        global p_array, m_array, v_array, labels

        self.ui.obj_list.clear()
        p_array = np.empty((0, 3))
        v_array = np.empty((0, 3))
        m_array = np.array([])
        labels = []

        self.ax.cla()
        self.ax.relim()  # Recalculate the limits
        self.ax.autoscale_view()
        self.canvas.draw()



    def add_array_data(self):

        global p_array, m_array, v_array, labels

        p1 = float(self.ui.pe1.text())
        p2 = float(self.ui.pe2.text())
        p3 = float(self.ui.pe3.text())

        p_data = np.array([[p1, p2, p3]])


        print(p_data)
        p_array = np.append(p_array, p_data, axis=0)
        print(p_array)

        v1 = float(self.ui.ve1.text())
        v2 = float(self.ui.ve2.text())
        v3 = float(self.ui.ve3.text())

        v_data = np.array([[v1, v2, v3]])

        print(v_data)
        v_array = np.append(v_array, p_data, axis=0)

        m = self.ui.mass_edit.text()
        m_array = np.append(m_array, float(m))

        lbl = self.ui.obj_name.text()
        labels.append(lbl)


        self.ui.obj_list.addItem(lbl)

        self.ui.pe1.clear()
        self.ui.pe2.clear()
        self.ui.pe3.clear()

        self.ui.ve1.clear()
        self.ui.ve2.clear()
        self.ui.ve3.clear()

        self.ui.mass_edit.clear()
        self.ui.obj_name.clear()

        print("data added")



    def remove_layout(self):
        print("layoyt")

        self.ax.cla()
        self.ax.relim()  # Recalculate the limits
        self.ax.autoscale_view()
        self.canvas.draw()






    def generate_plot(self):
        
        global G
        global legend_val

        self.g_val_change()

        print(G)


        self.plot_show(legend_val, G, dt)





    def g_val_change(self):

        global G

        G = float(self.ui.dt_edit.text())

        print(G)

        #self.plot_show(legend_val, G)

    def dt_val_change(self):

        global dt

        dt = float(self.ui.g_edit.text())

        print(dt)

        #self.plot_show(legend_val, G)


    def legend_val_change(self):

        global legend_val

        print("sss")



        if self.ui.legend_chk.isChecked():

            legend_val = True

            print(legend_val)

        else:

            legend_val = False
            print(legend_val)

        #self.plot_show(legend_val, G





    def plot_show(self, legend_val, G, dt):

        global p_array, m_array, v_array, labels

        # Create a 3D plot

        self.toolbar = NavigationToolbar(self.canvas,self)

        self.ax.cla()
        self.ax.relim()  # Recalculate the limits
        self.ax.autoscale_view()
        self.canvas.draw()


        # Define the initial conditions (positions, velocities, masses) for the Sun and the planets
        positions = p_array

        velocities = v_array

        masses = m_array

        # Celestial body labels
        labels = labels

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


        # Plot the trajectory as elliptical paths and add a legend
        for i in range(num_bodies):

            self.ax.plot(trajectory[i, :, 0], trajectory[i, :, 1], trajectory[i, :, 2], label=labels[i])

            # Plot the last position as a circular marker
            self.ax.scatter(trajectory[i, -1, 0], trajectory[i, -1, 1], trajectory[i, -1, 2], s=10, color='black')

        # Set labels and title
        self.ax.set_xlabel(self.ui.x_lbl.text())
        self.ax.set_ylabel(self.ui.y_lbl.text())
        self.ax.set_zlabel(self.ui.z_lbl.text())
        #ax.set_title('Solar System Simulation')


        # Add a legend in the top right corner



        self.ax.legend(loc='best')

        self.ax.legend().set_visible(legend_val)
        #self.canvas.se


        # Show the plot
        #plt.show()





        self.lay = QVBoxLayout()
        #self.lay.addWidget(self.toolbar)
        self.lay.addWidget(self.canvas)

        self.lay1 = QVBoxLayout()
        self.lay1.addWidget(self.toolbar)

        self.ui.plot_top.setLayout(self.lay)
        self.ui.nav_bar.setLayout(self.lay1)
        #self.ui.plot_screen.setVisible(True)





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
