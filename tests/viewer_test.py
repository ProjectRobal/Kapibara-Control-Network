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

pygame.init()

mode=pygame.display.set_mode((1600,600))

view=NeuralViewer(mode,network1)

NeuronPage(view.objects,network1)

Run=True

while Run:

    for event in pygame.event.get():
        if event.type==QUIT:
            Run=False

        view.event_loop(event)

    mode.fill((255,255,255))

    view.update()

    pygame.display.update()

pygame.quit()