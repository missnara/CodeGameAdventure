import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class GearMesh():
    
    def __init__(self) -> None:
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
        
        fig, ax = plt.subplots()

        for center in zip(self.indices[1], self.indices[0]):
            circle = patches.Circle(center, 0.9, fill=True, alpha=0.5, color='blue', linewidth=2)
            ax.add_patch(circle)
            
            
        ax.set_aspect('equal')
        ax.set_xlim(-1, 9)
        ax.set_ylim(-1, 9)
        ax.axis('off')