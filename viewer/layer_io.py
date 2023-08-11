from .baseobject import BaseObject
from .base import Nodes


class Layer_Inputs(BaseObject):
    def __init__(self,layer,position:tuple[int,int],nodes_radius:int,color:tuple[int,int,int],text_color:tuple[int,int,int]=(0,0,0)) -> None:
        super().__init__()
        self.layer=layer
        self.positon=position
        self.nodes_number:int=layer.input_size
        self.def_position=(int((position[0]-(self.nodes_number/2)*nodes_radius)),position[1])
        self.nodes=Nodes(self.def_position,nodes_radius,text_color,color)

    def draw(self,view):
        
        self.nodes.center=self.def_position
        
        for i in range(self.nodes_number):
            self.nodes.center=(self.def_position[0]+i*self.nodes.radius,self.def_position[1])
            self.nodes.setNumber(self.layer.inputs[i])
            self.nodes.draw(view)

class Layer_Outputs(BaseObject):
    def __init__(self,layer,position:tuple[int,int],nodes_radius:int,color:tuple[int,int,int],text_color:tuple[int,int,int]=(0,0,0)) -> None:
        super().__init__()
        self.layer=layer
        self.positon=position
        self.nodes_number:int=layer.output_size
        self.def_position=(int((position[0]-(self.nodes_number/2)*nodes_radius)),position[1])
        self.nodes=Nodes(self.def_position,nodes_radius,text_color,color)

    def draw(self,view):
        
        self.nodes.center=self.def_position
        
        for i in range(self.nodes_number):
            self.nodes.center=(self.def_position[0]+i*self.nodes.radius,self.def_position[1])
            self.nodes.setNumber(self.layer.last_outputs[i])
            self.nodes.draw(view)

