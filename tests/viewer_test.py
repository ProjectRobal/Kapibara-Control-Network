import numpy as np

import pygame
from pygame.locals import *
from viewer.viewer import NeuralViewer
import network

from viewer.button import Button

import viewer.base as base
from viewer.block import Block
from viewer.layer_io import Layer_Inputs,Layer_Outputs

from viewer.neuron_pages import NeuronPage

network1=network.Network(6)

network1.addLayer(256,32)
network1.addLayer(2,16)

network1.step(np.random.random(6))

class CameraView:
    '''
    An object that will zoom in/out and
    move 
    '''
    def __init__(self,width:int,height:int):
        self.width=width
        self.height=height
        self.gen_surface()
    
    def gen_surface(self):
        self._surface=pygame.Surface((self.width,self.height))

    def zoom(self,zoom:float):
        if zoom < 0:
            return

        self.width=int(np.clip(self.width*zoom,100,2000))
        self.height=int(np.clip(self.height*zoom,100,2000))
        self.gen_surface()

    def surface(self):
        return self._surface
    
    def blit(self,mode:pygame.Surface):

        image=pygame.transform.scale(self.surface(),mode.get_size())
        
        mode.blit(image,(0,0))

pygame.init()

camera=CameraView(2000,2000)

mode=pygame.display.set_mode((800,600),pygame.RESIZABLE)

view=NeuralViewer(network1)

NeuronPage(view.objects,network1)

Run=True

key_pressed=False

while Run:

    for event in pygame.event.get():
        if event.type==QUIT:
            Run=False

        if event.type==KEYDOWN:
            if not key_pressed:
                key_pressed=True
            if event.key == pygame.K_q:
                    camera.zoom(0.9)
            if event.key == pygame.K_e:
                    camera.zoom(1.1)

        if event.type==KEYUP:
            if  key_pressed:
                key_pressed=False


        view.event_loop(event)

    mode.fill((255,255,255))

    camera.surface().fill((255,255,255))

    view.update(camera.surface())

    camera.blit(mode)

    pygame.display.update()

pygame.quit()