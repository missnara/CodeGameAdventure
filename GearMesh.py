import random
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
        a 2D numpy array of zeros and colors
        non-zero indices are the coordinates of gears centriods in the mesh
    indices : tuple of np.array
        indices of the non-zero elements in the mesh

    Methods
    -------
    draw():
        Plots the gear mesh using matplotlib.
    __eq__(): -> boolean
    _get_neighbors(gear_idx): -> tuple
        private returns all the valid neighbors
    action(gear_idx): -> boolean
        rotates the neighboring gears clockwise,
        returns True if the action possible, False if not
    """

    def __init__(self, colored_gears=3, color='#c57ebb') -> None:
        """
        Initializes the GearMesh with hardwired mesh configuration.
        """
        # 2D array represents the gear mesh. 1 indicates the center of a gear
        self.mesh = np.array([
            [None, None, '#00c7fd', None, '#00c7fd', None, '#00c7fd', None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, '#00c7fd', None, '#00c7fd', None, '#00c7fd', None, '#00c7fd', None],
            [None, None, None, None, None, None, None, None, None],
            ['#00c7fd', None, '#00c7fd', None, '#00c7fd', None, '#00c7fd', None, '#00c7fd'],
            [None, None, None, None, None, None, None, None, None],
            [None, '#00c7fd', None, '#00c7fd', None, '#00c7fd', None, '#00c7fd', None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, '#00c7fd', None, '#00c7fd', None, '#00c7fd', None, None]
            ])

        self.indices = tuple(map(tuple, np.argwhere(self.mesh != None)))
        selected_indices = random.sample(self.indices, colored_gears)
        rows, cols = zip(*selected_indices)
        self.mesh[rows, cols] = color

    def draw(self):
        """
        Draw the gear mesh using circles on a plot.
        """
        fig, ax = plt.subplots()
        for i, j in self.indices:
            # converting indices to coordinates for matplotlib
            x, y = j, -i
            circle = patches.Circle((x, y), 0.9, fill=True, alpha=0.5, color=self.mesh[i, j], linewidth=2)
            ax.add_patch(circle)
            ax.annotate(f"{(i,j)}", (x, y),
                        textcoords="offset points",
                        xytext=(0, 10),
                        ha='center')

        ax.set_aspect('equal')
        ax.set_xlim(-1, 9)
        ax.set_ylim(-9, 1)
        ax.axis('off')
        return fig, ax

    def _highlight_action(self, gear_idx):
        fig, ax = self.draw()
        y, x = gear_idx
        circle = patches.Circle((x, y), 0.95, fill=False, color='red', linewidth=2, linestyle=':')
        ax.add_patch(circle)
        print(self.indices[0])
        return fig, ax


    def __eq__(self, other):
        if isinstance(other, GearMesh):
            return np.array_equal(self.mesh, other.mesh)
        return False

    def _get_neighbors(self, gear_idx):
        if gear_idx not in self.indices:
            raise IndexError('This is not a gear index.')
        i, j = gear_idx
        neighbors = ((i-2, j-1), (i, j-2), (i+2, j-1), (i+2, j+1), (i, j+2), (i-2, j+1))
        valid_neighbors = [(a, b) for (a, b) in neighbors if (a, b) in self.indices]
        return tuple(valid_neighbors)

    def action(self, gear_idx, direction=None):
        if gear_idx not in self.indices:
            raise IndexError('This is not a gear index.')
        neighbors = self._get_neighbors(gear_idx)
        if len(neighbors) == 6:
            temp = self.mesh[neighbors[0][0], neighbors[0][1]]
            for i in range(1, 6):
                self.mesh[neighbors[i-1][0]][neighbors[i-1][1]] = self.mesh[neighbors[i][0]][neighbors[i][1]]
            self.mesh[neighbors[-1][0]][neighbors[-1][1]] = temp
            return True

        return False
