import pygame
from viewer.baseobject import BaseObject
from .page import Page
from . import base


class NeuronPage(Page):
    '''
        A page that initialize network view.
    '''
    def __init__(self, objects: list[BaseObject], network) -> None:
        super().__init__(objects, network)

        base_width=100
        base_height=200
        base_offset_y=50
        base_offset_x=50

        layer_offset_y=200

        for i,layer in enumerate(network.layers):
            rect=base.Rectangle(pygame.Rect(0,i*(layer_offset_y+base_height+base_offset_y*2),len(layer.blocks)*base_width)+base_offset_x,base_height+base_offset_y*2)
