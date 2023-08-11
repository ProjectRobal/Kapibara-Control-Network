import pygame
from viewer.baseobject import BaseObject
from .page import Page
from .block import Block
from . import base
from .layer_io import Layer_Inputs,Layer_Outputs


class NeuronPage(Page):
    '''
        A page that initialize network view.
    '''
    def __init__(self, objects: list[BaseObject], network) -> None:
        super().__init__(objects, network)

        base_width=200
        base_height=200
        base_offset_y=50
        base_offset_x=50

        layer_offset_y=200

        for i,layer in enumerate(network.layers):
            _width=int(len(layer.blocks)*base_width)+base_offset_x
            dy=int(i*(layer_offset_y+base_height+base_offset_y*2))
            layer_name="Layer: "+str(i+1)
            label=base.Label(pygame.Rect(-len(layer_name)*10,int(dy+base_height/2),100,50),layer_name,(0,0,0))
            rect=base.Rectangle(pygame.Rect(0,dy,_width,int(base_height+base_offset_y*2)),(255,0,0))
            layer_input=Layer_Inputs(layer,(_width/2,int(dy-50)),10,(255,0,0))
            layer_outputs=Layer_Outputs(layer,(_width/2,int(dy+base_height+base_offset_y*2)+50),10,(255,0,0))

            objects.append(rect)
            objects.append(label)
            objects.append(layer_input)
            objects.append(layer_outputs)

            for o,block in enumerate(layer.blocks):
                b_y=int(i*(layer_offset_y+base_height+base_offset_y*2))
                _block=Block(block,base.Rectangle(pygame.Rect(base_offset_x+o*(base_width+20),b_y,base_width,base_height),(0,0,255)),(0,255,0))
                objects.append(_block)
