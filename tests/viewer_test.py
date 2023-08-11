
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

pygame.init()

mode=pygame.display.set_mode((800,600))

view=NeuralViewer(mode,network1)

button=Button(pygame.rect.Rect(0,0,200,200),"Hello",(255,0,0),(0,0,0))

label=base.Label(pygame.rect.Rect(50,300,50,50),"Stachu",(0,0,0))

rect=base.Rectangle(pygame.rect.Rect(50,300,50,50),(0,0,255))

node=base.Nodes((300,300),25,(0,0,0),(0,0,255))

layer_input=Layer_Inputs(network1.layers[0],(300,400),10,(255,0,0))

layer_output=Layer_Outputs(network1.layers[0],(300,350),10,(255,0,0))

network1.layers[0].blocks[0].pickBatch()

block_test=Block(network1.layers[0].blocks[0],rect,(0,255,0))

button.on_click=lambda x: print("Hello world!")


view.objects.append(label)
view.objects.append(node)
view.objects.append(block_test)
view.objects.append(layer_input)
view.objects.append(layer_output)

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