
import pygame
from pygame.locals import *
from viewer.viewer import NeuralViewer
import network

from viewer.button import Button

import viewer.base as base

network1=network.Network(6)

network1.addLayer(256,32)
network1.addLayer(2,16)

pygame.init()

mode=pygame.display.set_mode((800,600))

view=NeuralViewer(mode,network1)

button=Button(pygame.rect.Rect(0,0,200,200),"Hello",(255,0,0),(0,0,0))

label=base.Label(pygame.rect.Rect(50,300,50,50),"Stachu",(0,0,0))

rect=base.Rectangle(pygame.rect.Rect(50,300,50,50),(0,0,255))

button.on_click=lambda x: print("Hello world!")

view.objects.append(button)
view.objects.append(rect)
view.objects.append(label)

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