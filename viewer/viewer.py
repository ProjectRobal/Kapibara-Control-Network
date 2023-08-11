'''
An addon made in pygame to show in real time state of neural network.

It will be divided into subpages.

First will show topology of the network.
It will show each layers with outputs nodes and inputs nodes.

Second will show each blocks populations with respected neurons.

'''

import pygame
from pygame.locals import *
from network import Network
from .baseobject import BaseObject
from .page import Page

class NeuralViewer:
    def __init__(self,view:pygame.Surface,network:Network) -> None:
        '''
        view - a pygame application view used for rendering network view.
        network - a network wich is going to visualize by class
        '''
        self.view=view
        self.network=network
        self.objects:list[BaseObject]=[]

    def event_loop(self,event:pygame.event.Event):
        '''
        event - a pygame event passed by event loop
        Need mainly for mouse event processing
        '''
        if event.type==MOUSEMOTION:
            for obj in self.objects:
                obj.on_mouse_cord(pygame.mouse.get_pos())
        elif event.type==MOUSEBUTTONUP:
            for obj in self.objects:
                obj.mouse_relased()
        elif event.type==MOUSEBUTTONDOWN:
            for obj in self.objects:
                if pygame.mouse.get_pressed(3)[0]:
                    obj.mouse_click(pygame.mouse.get_pos())
            

    def update(self):
        '''
        Class main routine in wich network will be drawn
        '''
        for obj in self.objects:
            obj.draw(self.view)
