import pygame
from viewer.baseobject import BaseObject
from .page import Page
from .block import Block
from . import base


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
            rect=base.Rectangle(pygame.Rect(0,int(i*(layer_offset_y+base_height+base_offset_y*2)),int(len(layer.blocks)*base_width)+base_offset_x,int(base_height+base_offset_y*2)),(255,0,0))
            objects.append(rect)

            for o,block in enumerate(layer.blocks):
                b_y=int(i*(layer_offset_y+base_height+base_offset_y*2))
                _block=Block(block,base.Rectangle(pygame.Rect(base_offset_x+o*(base_width+20),b_y,base_width,base_height),(0,0,255)),(0,255,0))
                objects.append(_block)
