import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class GearMesh:
    """
    A class to represent the game as a mesh of gears.
    clicking on one gear, makes all the 6 neighbouring gears to rotate.
    The original game has 19 gears
    ...

    Attributes
    ----------
    mesh : np.array
        a 2D numpy array of zeros and ones 
        non-zero elements indices are the coordinates of gears centriods in the mesh
    indices : tuple of np.array
        indices of the non-zero elements in the mesh

    Methods
    -------
    draw():
        Plots the gear mesh using matplotlib.
    """

    def __init__(self):
        """
        Initializes the GearMesh with hardwired mesh configuration.
        """
        # 2D array represents the gear mesh. 1 indicates the center of a gear
        self.mesh = np.array([[0., 0., 1., 0., 1., 0., 1., 0., 0.],
                              [0., 0., 0., 0., 0., 0., 0., 0., 0.],
                              [0., 1., 0., 1., 0., 1., 0., 1., 0.],
                              [0., 0., 0., 0., 0., 0., 0., 0., 0.],
                              [1., 0., 1., 0., 1., 0., 1., 0., 1.],
                              [0., 0., 0., 0., 0., 0., 0., 0., 0.],
                              [0., 1., 0., 1., 0., 1., 0., 1., 0.],
                              [0., 0., 0., 0., 0., 0., 0., 0., 0.],
                              [0., 0., 1., 0., 1., 0., 1., 0., 0.]])

        mask = self.mesh == 1
        self.indices = np.where(mask)

    def draw(self):
        """
        Draw the gear mesh using circles on a plot.
        """
        fig, ax = plt.subplots()

        # Plot circles in the positions of gears
        for center in zip(self.indices[1], self.indices[0]):
            circle = patches.Circle(center, radius=0.9, fill=True,
                                    alpha=0.5, color='blue', linewidth=2)
            ax.add_patch(circle)

        ax.set_aspect('equal')
        ax.set_xlim(-1, 9)
        ax.set_ylim(-1, 9)
        ax.axis('off')

        plt.show()

