import pygame

from .base import Rectangle
from .baseobject import BaseObject

class Block(BaseObject):
    def __init__(self,block,rect:Rectangle,color:tuple[int,int,int],res:float=1.0,neuron_radius:int=5) -> None:
        '''
        block - a block from network
        color - a color of every neurons
        '''
        super().__init__()
        self.rect=rect
        self.block=block
        self.color=color
        self.height_res=res
        self.n_radius=neuron_radius

    def draw(self,view):
        
        self.rect.draw(view)

        rect=self.rect.rect
        
        batch=self.block.batch

        dx=(rect.width/len(batch))+int(self.n_radius/2)

        for i in range(len(batch)):
            
            dy=(batch[i].evaluation/self.height_res)*rect.height

            pygame.draw.circle(view,self.color,
                               (int(rect.left+i*dx),rect.bottom-dy),
                               self.n_radius)

        
    
